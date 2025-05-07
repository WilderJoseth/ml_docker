import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from scripts import utils

PATH_DATA_OUT = os.path.join(os.getcwd(), "output/data")

categorical_features = ["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"]
numeric_features = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]
target_variable = "income"

def main(df):
    print("\n------------------ START ANALYSING DATA ------------------")
    explore(df)
    df_cleaned = clean(df)
    eda(df_cleaned)
    save(df_cleaned)
    print("\n------------------ END ANALYSING DATA ------------------")
    return df_cleaned
    
def explore(df):
    '''
        This is a first glance over the data
    '''
    print("\n------------------ START EXPLORING DATA ------------------")
    utils.save_columns_info("2_eda_initial", df.isnull().sum(), "Total missing by columns", "df_missing_values", True)

    print("\n--------- Start Categorical variables ---------")
    utils.save_columns_unique("2_eda_initial", df[categorical_features], "df_categorical_values", True)
    print("\n--------- End Categorical variables ---------")

    print("\n--------- Start Numerical variables ---------")
    utils.save_columns_info("2_eda_initial", df[numeric_features].describe(), "Describe", "df_numerical_values", True)
    print("\n--------- End Numerical variables ---------")

    print("\n--------- Start Target variable ---------")
    utils.save_columns_info("2_eda_initial", df[target_variable].unique(), "Target variable", "df_target_values", True)
    print("\n--------- End Target variable ---------")

    print("\n------------------ END EXPLORING DATA ------------------")

def clean(df):
    '''
        Clean data
    '''
    print("\n------------------ START CLEANING DATA ------------------")
    print("\n--------- Start Categorical variables ---------")
    print("\nRemove spaces and turn them capital")
    for c in categorical_features:
        df[c] = df[c].str.strip()
        df[c] = df[c].str.upper()

    print("\nRemove ? value")
    df.replace("?", np.nan, inplace = True)

    print("\nFill with the most frequent")
    si = SimpleImputer(strategy = "most_frequent")
    ar = si.fit_transform(df)
    df = pd.DataFrame(ar, columns = df.columns)
    print("\n--------- End Categorical variables ---------")

    print("\n--------- Start Target variable ---------")
    print("\nRemove spaces")
    df[target_variable] = df[target_variable].str.strip()
    df[target_variable].unique()
    print("\n--------- End Target variable ---------")

    utils.save_columns_unique("3_eda_cleaning", df[categorical_features], "df_categorical_values", True)
    utils.save_columns_info("3_eda_cleaning", df[target_variable].unique(), "Target variable", "df_target_values", True)
    utils.save_columns_info("3_eda_cleaning", df.isnull().sum(), "Total missing by columns", "df_missing_values")
    utils.save_dataframe_info("3_eda_cleaning", df)
    print("\n------------------ END CLEANING DATA ------------------")

    return df

def eda(df):
    '''
        Apply Exploratory Data Analysis
    '''
    print("\n------------------ START EDA ------------------")
    print("\n--------- Start Categorical variables ---------")
    # Distribution
    utils.save_chart_bar(df, "4_eda_categorical", "workclass")
    utils.save_chart_bar(df, "4_eda_categorical", "education")
    utils.save_chart_bar(df, "4_eda_categorical", "marital-status")
    utils.save_chart_bar(df, "4_eda_categorical", "occupation")
    utils.save_chart_bar(df, "4_eda_categorical", "relationship")
    utils.save_chart_bar(df, "4_eda_categorical", "race")
    utils.save_chart_bar(df, "4_eda_categorical", "sex")
    utils.save_chart_bar(df, "4_eda_categorical", "native-country")
    print("\n--------- End Categorical variables ---------")

    print("\n--------- Start Numerical variables ---------")
    utils.save_columns_info("5_eda_numerical", df[numeric_features].describe(), "Describe", "df_numerical_values", True)

    # Distribution
    utils.save_chart_box_histogram(df, "5_eda_numerical", "age", "income")
    utils.save_chart_box_histogram(df, "5_eda_numerical", "fnlwgt", "income")
    utils.save_chart_box_histogram(df, "5_eda_numerical", "education-num", "income")
    utils.save_chart_box_histogram(df, "5_eda_numerical", "capital-gain", "income")
    utils.save_chart_box_histogram(df, "5_eda_numerical", "capital-loss", "income")
    utils.save_chart_box_histogram(df, "5_eda_numerical", "hours-per-week", "income")

    # Relation and Correlation
    utils.save_chart_numeric_information(df[numeric_features], "5_eda_numerical")
    print("\n--------- End Numerical variables ---------")

    print("\n--------- Start Target Variable ---------")
    utils.save_chart_bar(df, f"4_eda_categorical", target_variable)
    print("\n--------- End Target Variable ---------")

    print("\n------------------ END EDA ------------------")

def save(df):
    '''
        Save dataframe
    '''
    print("\n------------------ START SAVE DATA ------------------")
    utils.save_dataset(df, "adult_cleaned.csv")
    print("\n------------------ END SAVE DATA ------------------")
