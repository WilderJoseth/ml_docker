import os
import pandas as pd
from scripts import utils

PATH_INPUT = os.path.join(os.getcwd(), "input")

def read():
    '''
        Read data from file
    '''
    print("\n------------------ START DATA EXTRACTION PROCESS ------------------")
    column_names = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", 
                    "hours-per-week", "native-country", "income"]

    df = pd.read_csv(os.path.join(PATH_INPUT, "adult.data"), header = None)
    df.columns = column_names
    
    utils.save_dataframe_info("1_initial_read", df)
    print("\n------------------ END DATA EXTRACTION PROCESS ------------------")

    return df
