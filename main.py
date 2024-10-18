import streamlit as st
from src.pipeline import suggestion_pipeline


# Title of the app
st.title("Email Suggestion")

# Input for previous history
previous_history = st.text_area("Enter Previous History:", height=15)

# Input for manifest
manifest = st.text_area("Enter Manifest:", height=15)

# Button to process inputs
if st.button("Submit"):

    respo = suggestion_pipeline(previous_history, manifest)
    # Process the inputs (you can customize this part)
    response_1 = f"{respo.Response1}"
    response_2 = f"{respo.Response2}"
    
    # Create two columns
    col1, col2 = st.columns(2)

    # Display the responses in the respective columns
    with col1:
        st.text_area("Response 1", value=response_1, height=150)

    with col2:
        st.text_area("Response 2", value=response_2, height=150)