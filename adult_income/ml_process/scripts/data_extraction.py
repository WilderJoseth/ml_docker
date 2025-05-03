import os
import pandas as pd
from scripts import utils

PATH_DATA_IN = os.path.join(os.getcwd(), "data")

def read():
    '''
        Read data from file
    '''
    print("\n------------------ START DATA EXTRACTION PROCESS ------------------")
    column_names = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", 
                    "hours-per-week", "native-country", "income"]

    df = pd.read_csv(os.path.join(PATH_DATA_IN, "adult.data"), header = None)
    df.columns = column_names
    
    utils.save_mlflow_artifact_dataframe_info("initial_read", df)
    utils.save_dataset(df, "Adult Income", "income", "https://www.kaggle.com/datasets/wenruliu/adult-income-dataset")
    print("\n------------------ END DATA EXTRACTION PROCESS ------------------")

    return df
