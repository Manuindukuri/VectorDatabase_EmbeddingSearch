import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

host_ip_address = os.getenv("HOST_IP_ADDRESS")

# Load the CSV file containing form information
df = pd.read_csv('pages/Extracts.csv')

def extracted_content():
    st.title("Extracted Forms")
    options = ["", "Examination Brochure", "Application for registration or exemption from registration as a national securities exchange Form 1", "Regulation A Offering Statement", "Notification under Regulation E", "Annual Reports and Special Financial Reports", "Form and amendments for notice of registration as a national securities exchange for the sole purpose of trading security futures products", "Semiannual Report or Special Financial Report Pursuant to Regulation A", "Current Report Pursuant to Regulation A", "Exit Report Under Regulation A", "General form for registration of securities pursuant to Section 12(b) or (g)"]
    selected_option = st.selectbox("Select a SEC Government Website form", options)

    if selected_option:
        st.write("You selected:", selected_option)

        library = st.selectbox("Select a library", ["", "PyPdf", "Nougat"])
        if library != "":
            st.write("Selected Library:", library)

            if library == "PyPdf":
                # Map selected form to an index
                form_index_mapping = {
                    "Examination Brochure": 0,
                    "Application for registration or exemption from registration as a national securities exchange Form 1": 1,
                    "Regulation A Offering Statement": 2,
                    "Notification under Regulation E": 3,
                    "Annual Reports and Special Financial Reports": 4,
                    "Form and amendments for notice of registration as a national securities exchange for the sole purpose of trading security futures products": 5,
                    "Semiannual Report or Special Financial Report Pursuant to Regulation A": 6,
                    "Current Report Pursuant to Regulation A": 7,
                    "Exit Report Under Regulation A": 8,
                    "General form for registration of securities pursuant to Section 12(b) or (g)": 9
                }
                form_index = form_index_mapping.get(selected_option)

                if form_index is not None:
                    st.info(f"You selected {selected_option} with the PyPdf library. Here's a summary:")
                    st.write(df.loc[df['Index'] == form_index]['content'].values[0])
                else:
                    st.warning("Please select a valid option with the PyPdf library.")

            elif library == "Nougat":
                # Map selected form to an index
                form_index_mapping = {
                    "Examination Brochure": 0,
                    "Application for registration or exemption from registration as a national securities exchange Form 1": 1,
                    "Regulation A Offering Statement": 2,
                    "Notification under Regulation E": 3,
                    "Annual Reports and Special Financial Reports": 4,
                    "Form and amendments for notice of registration as a national securities exchange for the sole purpose of trading security futures products": 5,
                    "Semiannual Report or Special Financial Report Pursuant to Regulation A": 6,
                    "Current Report Pursuant to Regulation A": 7,
                    "Exit Report Under Regulation A": 8,
                    "General form for registration of securities pursuant to Section 12(b) or (g)": 9
                }
                form_index = form_index_mapping.get(selected_option)

                if form_index is not None:
                    st.info(f"You selected {selected_option} with the Nougat library. Here's a summary:")
                    st.write(df.loc[df['Index'] == form_index]['nougat_content'].values[0])
                else:
                    st.warning("Please select a valid option with the Nougat library.")

# If the user is authenticated, they can access protected data
if "access_token" in st.session_state:
    access_token = st.session_state.access_token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(f"http://{host_ip_address}:8000/protected", headers=headers)
    if response.status_code == 200:
        authenticated_user = response.json()
        extracted_content() 
else:
    st.text("Please login/register to access the Application.")

