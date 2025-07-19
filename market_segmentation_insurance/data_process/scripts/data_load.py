from scripts import utils

def main(df):
    '''
        Function that starts the whole process
    '''
    load(df)

def load(df):
    '''
        Save clean and transformed data into table
    '''
    print("\n------------------ START DATA LOADING PROCESS ------------------")
    utils.db_insert_query_from_dataframe(df, "public.eda_data")
    print("\n------------------ END DATA LOADING PROCESS ------------------")