import os
import pandas as pd
#from prefect import flow
from scripts import utils, config

PATH_INPUT = os.path.join(os.getcwd(), "input")

#@flow(name = "Read data workflow", retries = 2, retry_delay_seconds = 20, timeout_seconds = 30)
def read() -> pd.DataFrame:
    '''
        Read data from DB
    '''
    print("\n------------------ START DATA EXTRACTION PROCESS ------------------")
    columns = ", ".join(config.NUMERIC_FEATURES + config.CATEGORICAL_FEATURES)
    df = utils.db_execute_query(f"SELECT {columns} FROM public.eda_data;")
    print("Shape:", df.shape)
    print(df.head())
    print("\n------------------ END DATA EXTRACTION PROCESS ------------------")

    return df
