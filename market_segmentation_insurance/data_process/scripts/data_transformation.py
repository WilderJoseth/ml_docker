from scripts import utils

def main(df):
    data_profiling(df)
    df = cleaning(df)
    return df

def data_profiling(df):
    print("\n------------------ START DATA PROFILING PROCESS ------------------")
    identify_missing_values(df)
    print("\n------------------ END DATA PROFILING PROCESS ------------------")

def identify_missing_values(df):
    print("\n------------------ START IDENTIFYING MISSING VALUES PROCESS ------------------")
    df_missing_values = df.isnull().sum().to_frame().reset_index()
    df_missing_values.columns = ["FEATURE", "FREQUENCY"]
    utils.db_insert_query_from_dataframe(df_missing_values, "public.missing_values_summary")
    print("Information saved in public.missing_values_summary")
    print("\n------------------ END IDENTIFYING MISSING VALUES PROCESS ------------------")

def cleaning(df):
    print("\n------------------ START DATA CLEANING PROCESS ------------------")

    print("\n------------------ START FILLING MISSING VALUES PROCESS ------------------")
    df["MINIMUM_PAYMENTS"] = df["MINIMUM_PAYMENTS"].fillna(df["MINIMUM_PAYMENTS"].median())
    df["CREDIT_LIMIT"] = df["CREDIT_LIMIT"].fillna(df["CREDIT_LIMIT"].median())

    print("Value: median")
    print("Columns: MINIMUM_PAYMENTS and CREDIT_LIMIT")
    print("\n------------------ END FILLING MISSING VALUES PROCESS ------------------")

    print("\n------------------ START REMOVING HIGH CARDINALITY COLUMN ID PROCESS ------------------")
    df = df.drop(columns = "CUST_ID")
    print("\n------------------ END REMOVING HIGH CARDINALITY COLUMN ID PROCESS ------------------")
    
    print("\n------------------ END DATA CLEANING PROCESS ------------------")
    return df