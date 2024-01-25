**Welcome to our custom built application to explore vector databses for efficient embedding search to generate prompt based on user specified content and questions in a large language model**

# OPEN AI CHATBOT

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)](https://airflow.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-%232496ED?style=for-the-badge&logo=Docker&color=blue&logoColor=white)](https://www.docker.com)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Amazon AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-%23412991?style=for-the-badge&logo=OpenAI&logoColor=%23412991&color=red)](https://platform.openai.com/docs/api-reference/introduction)
[![Postgres](https://img.shields.io/badge/Postgres-%234169E1?style=for-the-badge&logo=PostgreSQL&logoColor=%234169E1&color=black)](https://www.postgresql.org)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com)

OPEN AI CHATBOT is a comprehensive project that combines two distinct pipelines for data acquisition and embedding generation using Apache Airflow and a client-facing application built with Streamlit and FastAPI. The project addresses a real-world scenario where we extract data and metadata from PDF files and store them in Pinecone, a vector database for efficient embedding search to prompt in large language model. The project answers to the question asked by the user using the GPT-3.5 Turbo model.

Documentation - https://codelabs-preview.appspot.com/?file_id=1D1rhMETWEnWB5HbrnLXo8uqPDJzaF3ZHa6dsZ0P6OKA#8

## Overview:

-**Pipeline 1:** Data Acquisition and Embedding Generation

Designed for data acquisition and embedding generation.
Parameters specified in YAML format include a list of PDF files for processing, chosen processing option (either "Nougat" or "PyPdf"), and credentials for processing.
Implements data validation checks to ensure accurate data parsing.
Generates embeddings and metadata for chunked texts.
Saves the extracted data in a CSV file into the S3 bucket for further use.

-**Pipeline 2:** Pinecone Database Integration

Parameterized source path of the CSV file from S3 bucket for loading into the Pinecone database.
Capable of creating, updating, and deleting the index as needed when data is refreshed.
This application is built using Streamlit and deployed on a Streamlit Cloud Platform. The project utilizes Amazon S3 for storage and Apache Airflow for managing the transcription workflow.

## Pages and features:

-**Login:** Users can login from this page. If the user is not registered, it will show invalid login details and the user will have to first register by accessing the register page.

-**Register:** Users can register on this page. Here we are implementing the user registration and login functionality with JWT authentication to secure API endpoints. After the registration is successrful, a confirmation email is sent to the email id which they entered while filling the details on the login page. After the registration is succesful, only then the user can see the view forms and ask me page.   

-**View Forms:** Users can select and view the SEC Government Forms available for display, then they can select the library from which they want to see the content. Depending upon which library i.e PYPDF or NOUGAT is chosen the user can view the extracted content of the form. 

-**Ask:** Allows users to input queries and utilizes Pinecone's Similarity search for information retrieval. It also supports 
filtering by form or querying across all items for comprehensive results. The model returns the answer to the query by using the GPT-3.5 Turbo model

# Project Tree

```
📦 
├─ .gitignore
├─ LICENSE
├─ Login.py
├─ README.md
├─ airflow
│  ├─ .DS_Store
│  ├─ dags
│  │  ├─ .DS_Store
│  │  ├─ cleaned_file.csv
│  │  ├─ dag_1.py
│  │  ├─ embeddings.csv
│  │  ├─ pipeline_1.py
│  │  └─ pipeline_2.py
│  ├─ docker-compose.yaml
│  └─ logs
│     └─ scheduler
│        └─ latest
├─ example_env.txt
├─ fast_api
│  ├─ Dockerfile
│  ├─ Pipfile
│  ├─ Pipfile.lock
│  ├─ requirements.txt
│  └─ user_registration.py
├─ pages
│  ├─ 1_Register.py
│  ├─ 2_ViewForms.py
│  ├─ 3_AskMe.py
│  ├─ Extracts.csv
│  ├─ image.jpg
│  └─ quotes.txt
└─ requirements.txt
```

# Prerequisites

To run this project, you will need:

- Postgres -14
- 'users' database and 'users' table with 'password' as password in Postgres14
- Enable CRUD operations for the database
- Google Cloud Platform account
- Docker
- Airflow
- AWS access and secret keys
- OpenAI API key
- .env file containing the AWS and OpenAI keys

# Installation & Workflow

- Clone the repository.
- Install the required packages by running pip install -r requirements.txt.
- Create a 'users' database and 'users' table with 'password' as password in Postgres14 in your machine.
- Enable CRUD operations for the database.
- Create your .env file by looking at the example_env file and ensure the .env file contains the AWS, OpenAI & Pinecone keys 
- Create a VM instance in Google Cloud Platform.
- Set up Airflow in the VM instance:
- Register as a user
- Run Airflow Pipeline 1 which will generate the embeddings & metadata for the chunked texts & save them in a CSV file into the S3 bucket.
- Login into your AWS account and check if the csv file is generated into your S3 bucket.
- Run Airflow Pipeline 2 for inserting the data from the csv file into the pinecone database.
- After successfully inserting the data into pinecone database return to the View Forms page.
- Select the from from the available list of SEC Government Forms and your library i.e PyPdf or Nougat to process the extracted content.
- Ask questions to the model from the ASK ME page which will search for the data from the pincone database and return an answer from the Open AI model by utilizing the GPT-3.5 Turbo model. 

### .env file for airflow:

```
AIRFLOW_UID=""
AWS_ACCESS_KEY=""
AWS_SECRET_KEY=""
S3_BUCKET_NAME=""
OPENAI_API_KEY=""
PINECONE_API_KEY=""
MY_EMAIL="Your email"
APP_PASSWORD="Your password"
OPENAI_KEY=""
PINECONE_API=""
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_HOST=""
POSTGRES_PORT="5432"
POSTGRES_DB=""
```

# Create virtual environment for streamlit

### Install virtualenv if you haven't already
```
pip install virtualenv
```

### Create a virtual environment
```
virtualenv myenv
```

### Create python environment for the directory
```
python -m venv myenv
```

### Activate the virtual environment
```
source myenv/bin/activate
```

### Pip install requirements
```
pip install -r requirements.txt
```

# Fast API

### Activate the shell
```
pipenv shell
```

### Install dependencies
```
pip install -r requirements.txt
```

### Start the server
```
uvicorn user_regstration:app --reload 
```

# Streamlit Installation & Activation

```
$ mkdir streamlit

$ cd streamlit 

$ mkdir .streamlit

$ python -m venv .streamlit 

$ source .streamlit/bin/activate

$ cd ..
```

### Run streamlit application
```
streamlit run Login.py
```

# Database Setup

- Create Table
```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    full_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    hashed_password VARCHAR(255),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

- Create user role
```
CREATE USER admin WITH PASSWORD 'password';
```

- Grant necessary privileges for generating primary key values
```
GRANT USAGE, SELECT ON SEQUENCE users_id_seq TO admin;
```

- Admin role can perform all CRUD operations
```
GRANT SELECT, INSERT, UPDATE, DELETE ON users TO admin;
```

## License
This project is licensed under the MIT License.
