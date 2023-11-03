from fastapi import FastAPI
from pydantic import BaseModel
import openai
import pinecone
app = FastAPI()
api_key = "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"
EMBEDDING_MODEL = "text-embedding-ada-002"
pinecone_api_key = "b4337a10-efc0-4747-8b3c-5469b1485320"
pinecone.init(api_key=pinecone_api_key)

class UserInput(BaseModel):
    form: str
    question: str

def generate_embeddings(question: str):
    try:
        # Create embeddings for the given 'question' using the specified EMBEDDING_MODEL
        openai.api_key = api_key
        response = openai.Embedding.create(model=EMBEDDING_MODEL, input=question)
        # Extract the embeddings from the API response
        return response["data"][0]["embedding"]
    except Exception as e:
        return str(e)
    
def query_pinecone(selected_form, top_k):
    # Initialize Pinecone
    pinecone.init(api_key=pinecone_api_key, environment="gcp-starter")
    index = pinecone.Index(index_name='my-index')
    # Prepare the filter condition based on the selected form
    filter_condition = {"metadata.form_title": {"$eq": selected_form}}
    # Execute the query with the filter condition
    results = index.query("", top_k=top_k, include_metadata=True, filter=filter_condition)
    return results
    

@app.post("/process_question")
def process_question(input_data: UserInput):
    embeddings = generate_embeddings(input_data.question)
    if isinstance(embeddings, str):
        return {"error": embeddings}
    # Search Pinecone with the selected form title and user's question
    search_result = query_pinecone(input_data.form, top_k=1)
    return {"embeddings": embeddings, "pinecone_search_result": search_result}