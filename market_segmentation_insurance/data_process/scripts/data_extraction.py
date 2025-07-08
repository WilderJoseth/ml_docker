import os
import pandas as pd
from scripts import utils

PATH_INPUT = os.path.join(os.getcwd(), "input")

def read():
    print("\n------------------ START DATA READING PROCESS ------------------")
    df = pd.read_csv(os.path.join(PATH_INPUT, "Customer Data.csv"))
    print("Shape:", df.shape)
    print("\n------------------ END DATA READING PROCESS ------------------")

def save():
    print("\n------------------ START DATA SAVING PROCESS ------------------")
    query = "SELECT * FROM public.raw_data;"
    rows = utils.db_execute_query_select(query)
    print("\n------------------ END DATA SAVING PROCESS ------------------")