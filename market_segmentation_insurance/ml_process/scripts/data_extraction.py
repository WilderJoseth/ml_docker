import os
import pandas as pd
from prefect import flow
from scripts import config

PATH_INPUT = os.path.join(os.getcwd(), "input")

@flow(name = "Read data workflow", retries = 2, retry_delay_seconds = 20, timeout_seconds = 30)
def read() -> pd.DataFrame:
    '''
        Read data from file
    '''
    print("\n------------------ START DATA EXTRACTION PROCESS ------------------")
    df = pd.read_csv(os.path.join(PATH_INPUT, config.FILE_NAME_INPUT))
    print("\n------------------ END DATA EXTRACTION PROCESS ------------------")

    return df
