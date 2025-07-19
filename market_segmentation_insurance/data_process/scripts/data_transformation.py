import pandas as pd
from scripts import utils, config

def main(df):
    '''
        Function that starts the whole process
    '''
    data_profiling(df)
    df = change_data_type(df)
    df = cleaning(df)
    return df

def data_profiling(df):
    '''
        Function that starts profiling process
    '''
    print("\n------------------ START DATA PROFILING PROCESS ------------------")
    identify_missing_values(df)
    identify_duplicated_values(df)
    validate_data_consistency(df)
    print("\n------------------ END DATA PROFILING PROCESS ------------------")

def identify_missing_values(df):
    '''
        Function that identifies missing values in data
    '''
    print("\n------------------ START IDENTIFYING MISSING VALUES PROCESS ------------------")
    df_missing_values = df.isnull().sum().to_frame().reset_index()
    df_missing_values.columns = ["feature", "frequency"]
    utils.db_insert_query_from_dataframe(df_missing_values, "public.missing_values_summary")
    print("Information saved in public.missing_values_summary")
    print("\n------------------ END IDENTIFYING MISSING VALUES PROCESS ------------------")

def identify_duplicated_values(df):
    '''
        Function that identifies duplicated data
    '''
    print("\n------------------ START IDENTIFYING DUPLICATED VALUES PROCESS ------------------")
    total_duplicated = df.duplicated().sum()
    utils.db_execute_query(f"INSERT INTO public.data_profiling (total_duplicated) VALUES ({total_duplicated});")
    print("\n------------------ END IDENTIFYING DUPLICATED VALUES PROCESS ------------------")

def validate_data_consistency(df):
    '''
        Function that identifies if values matches with their data type
    '''
    print("\n------------------ START VALIDATING DATA CONSISTENCY PROCESS ------------------")
    print("\n------------------ START VALIDATING NUMERIC VALUES PROCESS ------------------")
    total_no_valid_list = []
    for c in config.NUMERIC_FEATURES:
        total_no_valid = df[c].apply(lambda x: not utils.validate_number(x)).sum()
        total_no_valid_list.append(total_no_valid)
    df_consistency = pd.DataFrame({"feature": config.NUMERIC_FEATURES, "total_no_valid": total_no_valid_list, "type_data": ["Numeric"] * len(config.NUMERIC_FEATURES)})
    utils.db_insert_query_from_dataframe(df_consistency, "public.data_consistency_summary")
    print("Information saved in public.data_consistency_summary")
    print("\n------------------ END VALIDATING NUMERIC VALUES PROCESS ------------------")
    print("\n------------------ END VALIDATING DATA CONSISTENCY PROCESS ------------------")

def change_data_type(df):
    '''
        Function that changes data type
    '''
    print("\n------------------ START CHANGE DATA TYPE PROCESS ------------------")
    for c in config.NUMERIC_FEATURES:
        df[c] = df[c].astype(float)
    print("\n------------------ END CHANGE DATA TYPE PROCESS ------------------")
    return df

def cleaning(df):
    '''
        Function that starts cleaning process
    '''
    print("\n------------------ START DATA CLEANING PROCESS ------------------")

    print("\n------------------ START FILLING MISSING VALUES PROCESS ------------------")
    df["minimum_payments"] = df["minimum_payments"].fillna(df["minimum_payments"].median())
    df["credit_limit"] = df["credit_limit"].fillna(df["credit_limit"].median())

    print("Value: median")
    print("Columns: minimum_payments and credit_limit")
    print("\n------------------ END FILLING MISSING VALUES PROCESS ------------------")

    print("\n------------------ START REMOVING HIGH CARDINALITY COLUMN ID PROCESS ------------------")
    df = df.drop(columns = "cust_id")
    print("\n------------------ END REMOVING HIGH CARDINALITY COLUMN ID PROCESS ------------------")
    
    print("\n------------------ END DATA CLEANING PROCESS ------------------")
    return df