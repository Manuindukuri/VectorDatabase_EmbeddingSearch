# import streamlit as st

# def questionnaire_login():
#     st.title("Open AI Chatbot")
#     options = ["","Examination Brochure", "Application for registration or exemption from registration as a national securities exchange Form 1", "Regulation A Offering Statement", "Notification under Regulation E", "Annual Reports and Special Financial Reports", "Form and amendments for notice of registration as a national securities exchange for the sole purpose of trading security futures products", "Semiannual Report or Special Financial Report Pursuant to Regulation A", "Current Report Pursuant to Regulation A", "Exit Report Under Regulation A","General form for registration of securities pursuant to Section 12(b) or (g)" ]
#     selected_option = st.selectbox("Select a SEC Government Website form", options)
    

#     if selected_option:
#         st.write("You selected:", selected_option)


#         library = st.selectbox("Select a library", ["","PyPdf", "Nougat"])
#         if library != "":
#             st.write("Selected Library:", library)

#             if library == "PyPdf":
#                 # Display summaries based on the selected option and PyPdf library
#                     if selected_option == "Examination Brochure":
#                         st.info("You selected Form 1 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Application for registration or exemption from registration as a national securities exchange Form 1":
#                         st.info("You selected Form 2 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Regulation A Offering Statement":
#                         st.info("You selected Form 3 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Notification under Regulation E":
#                         st.info("You selected Form 4 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Annual Reports and Special Financial Reports":
#                         st.info("You selected Form 5 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Form and amendments for notice of registration as a national securities exchange for the sole purpose of trading security futures products":
#                         st.info("You selected Form 6 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Semiannual Report or Special Financial Report Pursuant to Regulation A":
#                         st.info("You selected Form 7 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Current Report Pursuant to Regulation A":
#                         st.info("You selected Form 8 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "Exit Report Under Regulation A":
#                         st.info("You selected Form 9 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")
#                     elif selected_option == "General form for registration of securities pursuant to Section 12(b) or (g)":
#                         st.info("You selected Form 10 with the PyPdf library. Here's a summary for Form 1 using PyPdf.")



#             elif library == "Nougat":
#                 # Display summaries based on the selected option and Nougat library
#                     if selected_option == "Form 1":
#                         st.info("You selected Form 1 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 2":
#                         st.info("You selected Form 2 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 3":
#                         st.info("You selected Form 3 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 4":
#                         st.info("You selected Form 4 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 5":
#                         st.info("You selected Form 5 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 6":
#                         st.info("You selected Form 6 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 7":
#                         st.info("You selected Form 7 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 8":
#                         st.info("You selected Form 8 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 9":
#                         st.info("You selected Form 9 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     elif selected_option == "Form 10":
#                         st.info("You selected Form 10 with the Nougat library. Here's a summary for Form 1 using Nougat.")
#                     else:
#                         st.warning("Please select a valid option with the Nougat library.")

# if __name__ == "__main__":
#     questionnaire_login()



import streamlit as st
import pandas as pd

# Load the CSV file containing form information
df = pd.read_csv('/Users/prathamesh/Desktop/Github/Assignment-3/notebooks/summary1.csv')

def questionnaire_login():
    st.title("Open AI Chatbot")
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

if __name__ == "__main__":
    questionnaire_login()




