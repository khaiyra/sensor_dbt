import datetime as dt
import pandas as pd
import csv
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import mysql.connector as msql
from mysql.connector import Error
import os

def load_data(data):
    df = pd.read_csv(data)
    return df

def to_sql():
    new_df = load_data('station_summary.csv')
    try:
        #data = pd.read_csv(f'{CUR_DIR}/station_summary.csv')
        conn = msql.connect(host='localhost', database='sensor', user='root', password='password')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database:", record)
            #f = open (f'{CUR_DIR}/scripts/test.sql', 'a') 
            query = 'INSERT INTO stations (id, flow_99, flow_max, flow_median, flow_total, n_obs) VALUES'
            val = list(data.to_records(index=False))
            string = query + str(val).replace('[','').replace(']','')
            f.write(string)
            f.write(';')
            f.close()
    except Error as e:
        print("Error while connecting to MySQL", e)

# DAG's arguments
default_args = {
        'owner': 'Khaiyra',
        'start_date':dt.datetime(2021, 22, 9, 9, 0, 0),
        'concurrency': 1,
        'retries': 0
        }

# DAG's operators, or bones of the workflow
with DAG('Loading data into Database',
        catchup=False, # To skip any intervals we didn't run
        default_args=default_args,
        schedule_interval='* 1 * * * *', # 's m h d mo y'; set to run every minute.
        ) as dag:

    load_csv = PythonOperator(
            task_id='Load CSV',
            python_callable=load_data,
            )

    upload_csv_to_sql = PythonOperator(
            task_id='CSV to Database',
            python_callable=to_sql
            )

# The actual workflow
load_csv >> upload_csv_to_sql
