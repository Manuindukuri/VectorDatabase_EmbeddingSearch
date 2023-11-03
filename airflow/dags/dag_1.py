from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import pandas as pd
import boto3
from io import BytesIO
from dotenv import load_dotenv
from pipeline_1 import generate_embeddings
# aws_access_key_id, aws_secret_access_key, s3_bucket_name   # Import the generate_embeddings function
from airflow.models import Variable

load_dotenv()

api_key = os.getenv('AIRFLOW_VAR_OPENAI_API_KEY')

# Set your S3 credentials
aws_access_key_id = os.getenv('AIRFLOW_VAR_AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AIRFLOW_VAR_AWS_SECRET_KEY')
s3_bucket_name = os.getenv('AIRFLOW_VAR_S3_BUCKET_NAME')

# Define your default_args for the DAG
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 10, 30),  # Adjust the start date as needed
}

# Initialize the DAG
dag = DAG('pipeline_1', default_args=default_args, schedule_interval=None)

# Define a function to generate embeddings and save to S3 for 'pypdf_content'
def generate_pypdf_embeddings_and_save_to_s3(**kwargs):
    # Construct the path to the CSV file
    current_directory = os.path.dirname(os.path.abspath(__file__ or '.'))
    csv_file_path = os.path.join(current_directory, 'cleaned_file.csv')

    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    embeddings_pypdf = df['pypdf_content'].apply(lambda x: generate_embeddings(x) if x else None)


    # Drop rows where embeddings could not be generated (e.g., due to empty content)
    embeddings_pypdf = embeddings_pypdf.dropna()

    # Check if there are any valid rows left after the drop
    if not embeddings_pypdf.empty:
        # Create a DataFrame with the embeddings for 'pypdf_content'
        df_pypdf = pd.DataFrame({'embeddings': embeddings_pypdf})

        df_pypdf.rename(columns={'embeddings': 'embeddings'}, inplace=True)

        # Concatenate the 'heading', 'pypdf_content', and 'content' columns
        df_final = pd.concat([df['heading'], df['pypdf_content'], df_pypdf], axis=1)

        # Convert DataFrame to CSV content as bytes
        csv_content = df_final.to_csv(index=False).encode('utf-8')

        # Upload the embeddings for 'pypdf_content' to S3
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        s3.put_object(Bucket='a3-damg', Key='embeddings.csv', Body=csv_content)
    else:
        print("No valid embeddings for 'pypdf_content' to save.")

# Define the PythonOperator to run the generate_pypdf_embeddings_and_save_to_s3 function
run_script_task = PythonOperator(
    task_id='generate_pypdf_embeddings_and_save_to_s3',
    python_callable=generate_pypdf_embeddings_and_save_to_s3,
    provide_context=True,  # Pass the context to the function
    dag=dag
)

# Set up the task dependencies
run_script_task  # This task doesn't have any dependencies