import streamlit as st

def questionnaire_login():
    st.title("Open AI Chatbot")
    options = ["","Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Option 8", "Option 9","Option 10" ]
    selected_option = st.selectbox("Select a SEC Government Website form", options)
    

    if selected_option:
        st.write("You selected:", selected_option)


        library = st.selectbox("Select a library", ["","PyPdf", "Nougat"])
        if library != "":
            st.write("Selected Library:", library)

            if library == "PyPdf":
                # Display summaries based on the selected option and PyPdf library
                    if selected_option == "Option 1":
                        st.info("You selected Option 1 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 2":
                        st.info("You selected Option 2 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 3":
                        st.info("You selected Option 3 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 4":
                        st.info("You selected Option 4 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 5":
                        st.info("You selected Option 5 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 6":
                        st.info("You selected Option 6 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 7":
                        st.info("You selected Option 7 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 8":
                        st.info("You selected Option 8 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 9":
                        st.info("You selected Option 9 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")
                    elif selected_option == "Option 10":
                        st.info("You selected Option 10 with the PyPdf library. Here's a summary for Option 1 using PyPdf.")



            elif library == "Nougat":
                # Display summaries based on the selected option and Nougat library
                    if selected_option == "Option 1":
                        st.info("You selected Option 1 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 2":
                        st.info("You selected Option 2 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 3":
                        st.info("You selected Option 3 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 4":
                        st.info("You selected Option 4 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 5":
                        st.info("You selected Option 5 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 6":
                        st.info("You selected Option 6 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 7":
                        st.info("You selected Option 7 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 8":
                        st.info("You selected Option 8 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 9":
                        st.info("You selected Option 9 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    elif selected_option == "Option 10":
                        st.info("You selected Option 10 with the Nougat library. Here's a summary for Option 1 using Nougat.")
                    else:
                        st.warning("Please select a valid option with the Nougat library.")

if __name__ == "__main__":
    questionnaire_login()



