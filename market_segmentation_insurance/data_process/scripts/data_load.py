from scripts import utils

def main(df):
    load(df)

def load(df):
    print("\n------------------ START DATA LOADING PROCESS ------------------")
    utils.db_insert_query_from_dataframe(df, "public.eda_data")
    print("\n------------------ END DATA LOADING PROCESS ------------------")