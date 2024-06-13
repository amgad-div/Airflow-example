
"""


@author: Amgad
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from datetime import timedelta
import pandas as pd

default_args = {
'owner': 'Amgad',
'start_date': dt.datetime(2024, 4, 13),
'retries': 1,
'retry_delay': dt.timedelta(minutes=5),
}

#Define a functions that will perform the cleaning tasks.

def cleanScooter():       
    df=pd.read_csv('scooter.csv')
    df.drop(columns=['region_id'], inplace=True)
    df.columns=[x.lower() for x in df.columns]
    df['started_at']=pd.to_datetime(df['started_at'],
    format='%m/%d/%Y %H:%M')
    df.to_csv('cleanscooter.csv')


#Define a function thatread in the cleaned data
    #and filter based on a start and end date.

def filterData():
    
    df=pd.read_csv('cleanscooter.csv')
    fromd = '2019-05-23'
    tod='2019-06-03'
    tofrom = df[(df['started_at']>fromd)&
    (df['started_at']<tod)]
    tofrom.to_csv('may23-june3.csv')

with DAG('CleanData',
default_args=default_args,schedule_interval=timedelta(minutes=5)) as dag:
    # Define the tasks

    task_bash = BashOperator(
        task_id = "bash_task",
        bash_command = """
                echo "Hello from amgad lets start our basic airflow project"
                """
        )

    cleanData = PythonOperator(
            task_id='clean',
            python_callable=cleanScooter

        )
    selectData = PythonOperator(
        task_id= 'filter_data',
        python_callable = filterData

        )
    copyFile = BashOperator(
        task_id='copy',
        bash_command='cp /home/Amgad/may23-june3.csv /home/Amgad/Desktop'
        )
    
# Set task dependencies
task_bash >> cleanData >> selectData >> copyFile

