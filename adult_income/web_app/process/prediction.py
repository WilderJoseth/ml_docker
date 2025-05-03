import numpy as np
import pandas as pd

def get_transformer(path_transformer):
    '''
        Load transformer files
    '''
    import joblib
    
    with open(path_transformer, "rb") as transformer_file:
        transformer = joblib.load(transformer_file)

    return transformer

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