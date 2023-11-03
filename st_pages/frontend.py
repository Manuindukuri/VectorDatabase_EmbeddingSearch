import streamlit as st
import requests
import pandas as pd
import boto3
import openai


api_key = "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"

# Set your S3 credentials
aws_access_key_id = "AKIAQE5K2OLWTAPLD7MW"
aws_secret_access_key = "LhPFBtSo0kE7BSPDNK9Uy+ZkfSUp5glx+ulKY906"
s3_bucket_name = "airflow-a3"

csv_file_path = "embeddings.csv"
# Create a function to read the CSV file from S3
def read_csv_from_s3(bucket_name, file_path):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    obj = s3.get_object(Bucket=bucket_name, Key=file_path)
    df = pd.read_csv(obj['Body'])
    return df

# Streamlit app
st.title('OPEN AI Chatbot')

try:
    df = read_csv_from_s3(s3_bucket_name, csv_file_path)

    st.write("Embeddings Data:")
    st.write(df.head(10))

    # Display a dropdown with column headers
    form_names = ["EXAMINATION BROCHURE", "APPLICATION FOR REGISTRATION OR EXEMPTION  FORM 1", "ELIGIBILITY REQUIREMENTS FOR FORM 1A", "NOTIFICATION UNDER REGULATION E", "ANNUAL REPORTS AND SPECIAL FINANCIAL REPORTS", "FORM 1N AND AMENDMENTS FOR NOTICE OF REGISTRATION", "SEMIANNUAL REPORT PURSUANT TO REGULATION A", "CURRENT REPORT PURSUANT TO REGULATION A"]

    selected_form = st.selectbox('Select a form from above:', form_names)

# Display the selected form name
    st.write(f'Selected Form: {selected_form}')


    user_question = st.text_input("Ask a question:")
    
    # if user_question:
    #     # Use the OpenAI model to generate a response
    #     response = openai.Completion.create(
    #         engine="text-davinci-003",  # You can choose a different engine if needed
    #         prompt=user_question,
    #         max_tokens=100  # You can adjust this based on your desired response length
    #     )
    #     st.write("Chatbot's Response:")
    #     st.write(response.choices[0].text)

except Exception as e:
    st.error(f"Error: {e}")

