import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")

def db_execute_query(query):
    print("\n------------------ START QUERY EXECUTION ------------------")
    connection = psycopg2.connect(host = HOST, database = DATABASE, user = USER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    print("\n------------------ END QUERY EXECUTION ------------------")

def db_execute_query_select(query):
    print("\n------------------ START QUERY SELECT EXECUTION ------------------")
    connection = psycopg2.connect(host = HOST, database = DATABASE, user = USER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Total rows queried:", len(rows))
    cursor.close()
    connection.close()
    print("\n------------------ END QUERY SELECT EXECUTION ------------------")
    return rows