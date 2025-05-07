import os
import numpy as np
import pandas as pd

# Input object
PATH_INPUT = os.path.join(os.getcwd(), "input")

def get_transformer(transformer_name):
    '''
        Load transformer files
    '''
    import joblib
    
    with open(os.path.join(PATH_INPUT, "transformers", transformer_name), "rb") as transformer_file:
        transformer = joblib.load(transformer_file)

    return transformer

def get_model(model_name):
    '''
        Load model files
    '''
    import joblib
    
    with open(os.path.join(PATH_INPUT, "models", model_name), "rb") as model_file:
        model = joblib.load(model_file)

    return model

def get_data():
    return pd.read_csv(os.path.join(PATH_INPUT, "data", "adult_cleaned.csv"))
 
def prepare(data, categorical_transformer, numeric_transformer):
    '''
        Transform input data
    '''
    categorical_features = ["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"]
    numeric_features = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]

    data = pd.Series(data)
    encoded_categorical = categorical_transformer.transform(data.loc[categorical_features].values.reshape(1, -1))
    encoded_numerical = numeric_transformer.transform(data.loc[numeric_features].values.reshape(1, -1))

    return np.squeeze(encoded_categorical), np.squeeze(encoded_numerical)

def predict(data, model, categorical_transformer, numeric_transformer):
    '''
        Make prediction
    '''
    encoded_categorical, encoded_numerical = prepare(data, categorical_transformer, numeric_transformer)
    data = np.concatenate((encoded_numerical, encoded_categorical)).reshape(1, -1)
    prediction = model.predict(data)
    return "Income below or equal than 50K" if prediction == 0 else "Income above than 50K"