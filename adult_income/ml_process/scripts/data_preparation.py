import pandas as pd
from scripts import utils

categorical_features = ["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"]
numeric_features = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]
target_variable = "income"

def main(df):
    print("\n------------------ START PREPARING DATA ------------------")
    df_categorical = categorical(df[categorical_features], df[target_variable])
    df_numeric = numerical(df[numeric_features])
    df_target = target(df[target_variable])
    df_encoded = pd.concat([df_numeric, df_categorical, df_target], axis = 1)

    print("Shape df_encoded:", df_encoded.shape)
    print("\n------------------ END PREPARING DATA ------------------")
    return df_encoded

def categorical(df, df_target):
    '''
        Transform categorical variables using one-hot-encoder
    '''
    from scipy.stats import chi2_contingency
    from sklearn.preprocessing import OneHotEncoder

    print("\n------------------ START PREPARING CATEGORICAL DATA ------------------")
    hypothesis_results = []
    for c in categorical_features:
        contingency_table = pd.crosstab(df[c], df_target)
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        if p < 0.05:
            print(f"Reject the null hypothesis: There is a significant association between {c} and {target_variable}.")
            hypothesis_results.append(f"Reject the null hypothesis: There is a significant association between {c} and {target_variable}.")
        else:
            print(f"Fail to reject the null hypothesis: No significant association between {c} and {target_variable}.")
            hypothesis_results.append(f"Fail to reject the null hypothesis: No significant association between {c} and {target_variable}.")

    # Get transformer instance 
    # sparse_output = False to return the values as vectors
    # drop = first to remove first class, because the rest of classes are enough explanatory and reduce training time 
    onehot_encoder = OneHotEncoder(sparse_output = False, drop = "first")

    # Training
    encoded_features = onehot_encoder.fit_transform(df[categorical_features])

    # Turn result into a dataframe
    df_one_hot_encoder = pd.DataFrame(encoded_features, columns = onehot_encoder.get_feature_names_out())
    print("\n------------------ END PREPARING CATEGORICAL DATA ------------------")

    # Save the transformer file
    utils.save_data_transformers(onehot_encoder, "categorical_transformer")

    return df_one_hot_encoder

def numerical(df):
    '''
        Transform numerical variables using MinMaxScaler
    '''
    print("\n------------------ START PREPARING NUMERICAL DATA ------------------")
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    ar = scaler.fit_transform(df)
    df_numeric = pd.DataFrame(ar, columns = numeric_features)
    print("Shape df_encoded:", df_numeric.shape)
    print("\n------------------ END PREPARING NUMERICAL DATA ------------------")

    # Save the transformer file
    utils.save_data_transformers(scaler, "numerical_transformer")

    return df_numeric

def target(df):
    '''
        Transform target variable
    '''
    print("\n------------------ START PREPARING TARGET VARIABLE ------------------")
    df_t = df.map(lambda x: 0 if x == "<=50K" else 1)
    print("\n------------------ END PREPARING TARGET VARIABLE ------------------")
    return df_t
    