import os
import pandas as pd
#from prefect import flow
from scripts import utils, config

#@flow(name = "Read data workflow", retries = 2, retry_delay_seconds = 20, timeout_seconds = 30)
def read() -> pd.DataFrame:
    '''
        Read data from DB
    '''
    print("\n------------------ START DATA EXTRACTION PROCESS ------------------")
    features = config.NUMERIC_FEATURES + config.CATEGORICAL_FEATURES
    columns = ", ".join(features)
    rows = utils.db_execute_query_select(f"SELECT {columns} FROM public.eda_data;")
    df = pd.DataFrame(rows, columns = features)
    print("Shape:", df.shape)
    print(df.head())
    print("\n------------------ END DATA EXTRACTION PROCESS ------------------")

    return df
