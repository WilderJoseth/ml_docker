import os
import pandas as pd
from prefect import task
from scripts import config

PATH_INPUT = os.path.join(os.getcwd(), "input")

@task(name = "read data", description = "Read data from file", retries = 3, retry_delay_seconds = 60, tags = ["data_exploration"])
def read():
    '''
        Read data from file
    '''
    print("\n------------------ START DATA EXTRACTION PROCESS ------------------")
    df = pd.read_csv(os.path.join(PATH_INPUT, config.FILE_NAME_INPUT))
    print("\n------------------ END DATA EXTRACTION PROCESS ------------------")

    return df
