import os
import time
import psycopg2
import psycopg2.extras as extras
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
RETRIES_CONNECTION = int(os.getenv("RETRIES_CONNECTION"))
RETRIES_CONNECTION_SECONDS = int(os.getenv("RETRIES_CONNECTION_SECONDS"))

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
    print("\n------------------ START QUERY EXECUTION ------------------")
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    print("\n------------------ END QUERY EXECUTION ------------------")

def db_execute_query_select(query):
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