import os
import pickle
import time
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError
import psycopg2.extras as extras

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
    '''
        Function that gets connection
    '''
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
    '''
        Execute query like insert, update or delete
    '''
    print("\n------------------ START QUERY EXECUTION ------------------")
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    print("\n------------------ END QUERY EXECUTION ------------------")

def db_execute_query_select(query):
    '''
        Execute query select
    '''
    print("\n------------------ START QUERY SELECT EXECUTION ------------------")
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Total rows queried:", len(rows))
    cursor.close()
    connection.close()
    print("\n------------------ END QUERY SELECT EXECUTION ------------------")
    return rows

def db_insert_query_from_dataframe(df, table_name):
    '''
        Execute multiple inserts from dataframe
    '''
    print("\n------------------ START INSERT DATAFRAME EXECUTION ------------------")
    # Creating query
    tuples = [tuple(x) for x in df.to_numpy(dtype = object)]
    columns = ",".join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" % (table_name, columns)
    
    # Inserting data
    connection = db_connection()
    cursor = connection.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
    print("\n------------------ END INSERT DATAFRAME EXECUTION ------------------")

def verify_data_process_is_ready():
    '''
        Function that verifies if data process service is completed
    '''
    for i in range(1, RETRIES_CONNECTION + 1):
        rows = db_execute_query_select("SELECT is_done FROM public.process_data WHERE name = 'Data Process';")
        is_done = bool(rows[0][0])
        if is_done:
            print("Data process service is ready")
            return True
        else:
            print(f"Attempt {i}: Data process service is not ready yet, retrying in {RETRIES_CONNECTION_SECONDS} seconds...")
            time.sleep(RETRIES_CONNECTION_SECONDS)
    raise OperationalError("Data process service is not ready after multiple attempts.")

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
