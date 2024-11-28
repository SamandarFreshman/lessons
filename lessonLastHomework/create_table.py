import pyodbc
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from recording import recording

load_dotenv()


server = os.environ.get('SERVER_SOURCE')
database = os.environ.get('DATABASE')
driver = os.environ.get('DRIVER')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')


conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;Connection Timeout=30'


connection = pyodbc.connect(conn_str)
cursor = connection.cursor()


engine = create_engine(f'mssql+pyodbc:///?odbc_connect={conn_str}')


def create_table(file_path,table_name):
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip')
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        recording(f"Table {table_name} inserted successfully!")
    except Exception as e:
        recording(f"Error: {e}")