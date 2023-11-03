import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

host_ip_address = os.getenv("HOST_IP_ADDRESS")

# Streamlit UI
st.title("Welcome to our Application")

# User login
def login():
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if not login_username or not login_password:
            st.error("Username and password are required.")
        else:
            response = requests.post(
                f"http://{host_ip_address}:8000/token",
                data={"username": login_username, "password": login_password},
            )
            if response.status_code == 200:
                access_token = response.json().get("access_token")
                st.success("Login successful. You can access protected data.")
                st.session_state.access_token = access_token  # Store the access_token in session_state
            else:
                st.error("Login failed. Check your credentials.")

if __name__ == "__main__":
    login()
