import streamlit as st
import requests

st.title("User Registration")

# User registration
def registration():
    username = st.text_input("Username", key="reg_username")
    full_name = st.text_input("Full Name", key="full_name")
    email = st.text_input("Email", key="email")
    password = st.text_input("Password", type="password", key="reg_password")

    if st.button("Register"):
        if not username or not full_name or not email or not password:
            st.error("All fields are required.")
        else:
            response = requests.post(
                "http://localhost:8000/register",
                json={"username": username, "full_name": full_name, "email": email, "password": password},
            )
            if response.status_code == 200:
                st.success("Registration successful. You can now log in.")
            else:
                st.error("Registration failed. Username may already be taken.")
                
if __name__ == "__main__":
    registration()