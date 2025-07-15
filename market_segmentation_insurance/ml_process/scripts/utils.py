import os
import pickle
import time
import pandas as pd
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError
from scripts import config

load_dotenv()

HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
RETRIES_CONNECTION = int(os.getenv("RETRIES_CONNECTION"))
RETRIES_CONNECTION_SECONDS = int(os.getenv("RETRIES_CONNECTION_SECONDS"))

PATH_OUTPUT = os.path.join(os.getcwd(), "output")

def db_connection():
    for i in range(1, RETRIES_CONNECTION + 1):
        try:
            connection = psycopg2.connect(host = HOST, database = DATABASE, user = USER, password = PASSWORD, port = PORT)
            print("Connection successful!")
            return connection
        except OperationalError as e:
            print(f"Attempt {i}: Connection failed, retrying in {RETRIES_CONNECTION_SECONDS} seconds...")
            time.sleep(RETRIES_CONNECTION_SECONDS)
    raise OperationalError("Could not connect to the database after multiple attempts.")

def db_execute_query(query):
    print("\n------------------ START QUERY TO DATAFRAME EXECUTION ------------------")
    connection = db_connection()
    df = pd.read_sql_query(query, connection)
    connection.close()
    print("\n------------------ END QUERY TO DATAFRAME EXECUTION ------------------")
    return df

def verify_paths():
    '''
        Verify if paths exist, otherwise create directories
    '''
    print("\n------------------ Start verifying base paths ------------------")
    if not os.path.exists(PATH_OUTPUT):
        os.mkdir(PATH_OUTPUT)
    print("\n------------------ End verifying base paths ------------------")

def save_data_transformers(dt: object, name: str):
    '''
        Save data transformers like onehotencoder or numeric scaler
    '''

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "transformers")):
        os.mkdir(os.path.join(PATH_OUTPUT, "transformers"))

    # Save
    with open(os.path.join(PATH_OUTPUT, "transformers", f"{name}.pkl"), 'wb') as file:
        pickle.dump(dt, file)

    print(f"Transformer created {name}.pkl")

def save_model(model: object, name: str):
    '''
        Save models
    '''

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "models")):
        os.mkdir(os.path.join(PATH_OUTPUT, "models"))

    # Save
    with open(os.path.join(PATH_OUTPUT, "models", f"{name}.pkl"), 'wb') as file:
        pickle.dump(model, file)

    print(f"Model created {name}.pkl")
