import streamlit as st

# Define the correct username and password
correct_username = "your_username"
correct_password = "your_password"

# Create a Streamlit login page
def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Logged in as {}".format(username))
            st.sidebar.title("Welcome to Your App")
            # Add your app content here
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    login()