import os
import sys
import pandas as pd
from scripts import utils, config

PATH_INPUT = os.path.join(os.getcwd(), "input")
FILE_NAME = os.getenv("FILE_NAME")

def main():
    '''
        Function that starts the whole process
    '''
    df = read()
    save(df)
    return df

def read():
    '''
        Read data from CSV file
    '''
    file_path = os.path.join(PATH_INPUT, FILE_NAME)
    while True:
        if not os.path.isfile(file_path):
            print(f"File '{FILE_NAME}' was not found. Upload the file and try again.")
            choice = input("Do you want to try another file? (y/n): ").strip().lower()
            if choice != "y":
                sys.exit(1)
        else:
            print("\n------------------ START DATA READING PROCESS ------------------")
            df = pd.read_csv(file_path)
            df.columns = config.FEATURES
            print("Shape:", df.shape)
            print("\n------------------ END DATA READING PROCESS ------------------")
            return df

def save(df):
    '''
        Save dataframe into a table
    '''
    print("\n------------------ START DATA SAVING PROCESS ------------------")
    utils.db_insert_query_from_dataframe(df, "public.raw_data")
    print("\n------------------ END DATA SAVING PROCESS ------------------")