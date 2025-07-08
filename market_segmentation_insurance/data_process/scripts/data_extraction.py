import os
import pandas as pd
from scripts import utils

PATH_INPUT = os.path.join(os.getcwd(), "input")

def main():
    df = read()
    save(df)
    return df

def read():
    print("\n------------------ START DATA READING PROCESS ------------------")
    df = pd.read_csv(os.path.join(PATH_INPUT, "Customer Data.csv"))
    print("Shape:", df.shape)
    print("\n------------------ END DATA READING PROCESS ------------------")
    return df

def save(df):
    print("\n------------------ START DATA SAVING PROCESS ------------------")
    utils.db_insert_query_from_dataframe(df, "public.raw_data")
    print("\n------------------ END DATA SAVING PROCESS ------------------")