#from prefect import task, flow
import pandas as pd
import numpy as np
from scripts import config, utils

#@flow(name = "Preparation data workflow", retries = 3, retry_delay_seconds = 20, timeout_seconds = 30)
def main(df: pd.DataFrame) -> pd.DataFrame:
    print("\n------------------ START PREPARING DATA ------------------")
    df_prepared = preparation(df)
    print("\n------------------ END PREPARING DATA ------------------")
    return df_prepared

#@task(name = "Preparation data")
def preparation(df: pd.DataFrame) -> pd.DataFrame:
    print("\n------------------ START PREPARING DATA ------------------")
    df_numeric = numerical(df)
    df_numeric_pca = dimensionality_reduction(df_numeric)
    df_categorical = categorical(df)

    df_prepared = pd.concat([df_numeric_pca, df_categorical], axis = 1)
    print("Shape:", df_prepared.shape)
    print("\n------------------ END PREPARING DATA ------------------")
    return df_prepared

def numerical(df: pd.DataFrame) -> pd.DataFrame:
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import PowerTransformer

    print("\n------------------ START TRANSFORMING NUMERICAL DATA ------------------")
    print("\n------------------ START SCALING DATA ------------------")
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(df[config.NUMERIC_FEATURES].values)
    print("\n------------------ END SCALING DATA ------------------")
    
    print("\n------------------ START REMOVING SKEWNESS DATA ------------------")
    print("\n------------------ Applying yeo-johnson method ------------------")
    pt = PowerTransformer(method = "yeo-johnson", standardize = False)
    x_transformed = pt.fit_transform(x_scaled)
    df_numeric_no_skewness = pd.DataFrame(x_transformed, columns = config.NUMERIC_FEATURES)
    print("\n------------------ END REMOVING SKEWNESS DATA ------------------")
    
    print("Shape:", df_numeric_no_skewness.shape)

    utils.save_data_transformers(scaler, "numerical_scaler_transformer")
    utils.save_data_transformers(pt, "numerical_pt_transformer")
    print("\n------------------ END TRANSFORMING NUMERICAL DATA ------------------")
    return df_numeric_no_skewness

def categorical(df: pd.DataFrame) -> pd.DataFrame:
    from sklearn.preprocessing import OneHotEncoder

    print("\n------------------ START TRANSFORMING CATEGORICAL DATA ------------------")
    print("\n------------------ Applying OneHotEncoder method ------------------")
    onehot_encoder = OneHotEncoder(sparse_output = False, drop = "first")
    encoded_features = onehot_encoder.fit_transform(df[config.CATEGORICAL_FEATURES])
    df_one_hot_encoder = pd.DataFrame(encoded_features, columns = onehot_encoder.get_feature_names_out())
    print("Shape:", df_one_hot_encoder.shape)

    utils.save_data_transformers(onehot_encoder, "categorical_transformer")
    print("\n------------------ END TRANSFORMING CATEGORICAL DATA ------------------")
    return df_one_hot_encoder

def dimensionality_reduction(x_scaled: np.array) -> pd.DataFrame:
    from sklearn.decomposition import KernelPCA

    print("\n------------------ START DIMENSIONALITY REDUCTION ------------------")
    print("\n------------------ Applying Kernel PCA method ------------------")
    kernel_pca = KernelPCA(n_components = config.N_COMPONENTS_PCA, kernel = config.KERNEL_PCA)
    x_kernel_pca = kernel_pca.fit_transform(x_scaled)
    df_numeric_pca = pd.DataFrame(x_kernel_pca, columns = ["C" + str(c) for c in range(config.N_COMPONENTS_PCA)])
    print("Shape:", df_numeric_pca.shape)
    utils.save_data_transformers(kernel_pca, "numerical_pca_transformer")
    print("\n------------------ END DIMENSIONALITY REDUCTION ------------------")
    return df_numeric_pca
