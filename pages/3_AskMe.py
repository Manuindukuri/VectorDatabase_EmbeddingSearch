import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

host_ip_address = os.getenv("HOST_IP_ADDRESS")

def question_answer(access_token):
    st.title("OpenAI Chatbot")
    st.write("Select forms below that you want to query:")

    form_names = ["EXAMINATION BROCHURE", "APPLICATION FOR REGISTRATION OR EXEMPTION  FORM 1", "ELIGIBILITY REQUIREMENTS FOR FORM 1A", "NOTIFICATION UNDER REGULATION E", "ANNUAL REPORTS AND SPECIAL FINANCIAL REPORTS", "FORM 1N AND AMENDMENTS FOR NOTICE OF REGISTRATION", "SEMIANNUAL REPORT PURSUANT TO REGULATION A", "CURRENT REPORT PURSUANT TO REGULATION A"]

    selected_forms = st.multiselect("Select Forms:", form_names)

    if not selected_forms:
        st.write('Selected Forms: None')
        selected_forms = form_names
    else:
        st.write(f'Selected Forms: {", ".join(selected_forms)}')

    user_question = st.text_input("Ask a question:")
    if st.button("Submit"):
        if user_question:
            headers = {"Authorization": f"Bearer {access_token}"}
            data = {"forms": selected_forms, "question": user_question}
            response = requests.post(f"http://{host_ip_address}:8000/process_question", json=data, headers=headers)

            if response.status_code == 200:
                answer = response.json().get("answer")
                st.write(f"Answer: {answer}")
            else:
                st.write("Error: Unable to retrieve an answer.")
        else:
            st.write("Enter your question")

# Check if the user is authenticated
if "access_token" in st.session_state:
    access_token = st.session_state.access_token
    question_answer(access_token)
else:
    st.text("Please login/register to access the Application.")
