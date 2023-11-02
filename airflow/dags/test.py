from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime,timedelta
from ast import literal_eval
import pandas as pd
import pinecone
import os
import time
global index


def csv_to_dataframe():
# Get the current working directory (where the DAG file is located)
    current_directory = os.path.dirname(os.path.abspath(__file__ or '.'))
    csv_file_path = os.path.join(current_directory, "new_embeddings.csv")
    df = pd.read_csv(csv_file_path)
    df.insert(0, 'id', range(1, len(df) + 1))
    df['id'] = df['id'].apply(str)
    df['embeddings'] = df['embeddings'].apply(literal_eval)
    df['heading'] = df['heading'].apply(str)
    
    return df


def connect_to_pinecone():
    index_name = 'my-index'
    # Initialize Pinecone client
    pinecone.init(api_key='b4337a10-efc0-4747-8b3c-5469b1485320',      
    environment='gcp-starter')     
    # Check whether the index with the same name already exists - if so, delete it
    if index_name in pinecone.list_indexes():
        pinecone.delete_index(index_name)
    pinecone.create_index(name=index_name, dimension=1536)
    index = pinecone.Index(index_name=index_name) 
    time.sleep(10)
    



def upsert_data_to_pinecone(**kwargs):
    global index
    ti = kwargs["ti"]
    df = ti.xcom_pull(task_ids="csv_to_dataframe_task")
    pinecone.init(api_key='b4337a10-efc0-4747-8b3c-5469b1485320',      
    environment='gcp-starter')    
    index = pinecone.Index(index_name="my-index") 
    for _, row in df.iterrows():
        r_id = str(row['id'])
        embedding = row['embeddings']
        heading = row['heading']

        meta={
            'form_title':heading,
        }

        index.upsert(vectors=[(r_id, embedding,meta)])
    time.sleep(10)
    

def validation():
    time.sleep(10)
    pinecone.init(api_key='b4337a10-efc0-4747-8b3c-5469b1485320',environment='gcp-starter')    
    index = pinecone.Index(index_name="my-index") 
    stats=index.describe_index_stats()
    print(f"Stats are : {stats}")


dag= DAG(
    dag_id= "v07",
    schedule= "0 0 * * *",
    start_date=days_ago(0),
    dagrun_timeout= timedelta(minutes=60),
    tags=["labs","damg7245"],
)
with dag:
    # Define PythonOperators for each task
    csv_to_dataframe_task = PythonOperator(
        task_id='csv_to_dataframe_task',
        python_callable=csv_to_dataframe
    )

    connect_to_pinecone_task = PythonOperator(
        task_id='connect_to_pinecone_task',
        python_callable=connect_to_pinecone

    )
    upsert_to_pinecone_task = PythonOperator(
        task_id='upsert_to_pinecone_task',
        python_callable=upsert_data_to_pinecone
    )
    validation_task = PythonOperator(
        task_id='validation_task',
        python_callable=validation
    )


    csv_to_dataframe_task >> connect_to_pinecone_task >> upsert_to_pinecone_task >> validation_task







