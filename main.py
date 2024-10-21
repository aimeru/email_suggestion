import streamlit as st
import asyncio
from src.pipeline import suggestion_pipeline
from src.models import AiResponse

st.title("Email Suggestion")
previous_history = st.text_area("Enter Previous History:", height=150)
manifest = st.text_area("Enter Manifest:", height=150)

async def main():
    try:
        respo: AiResponse = await suggestion_pipeline(previous_history, manifest)
        if respo and hasattr(respo, 'Response1') and hasattr(respo, 'Response2'):
            response_1 = respo.Response1
            response_2 = respo.Response2

            col1, col2 = st.columns(2)
            with col1:
                st.text_area("Response 1", value=response_1, height=500)
            with col2:
                st.text_area("Response 2", value=response_2, height=500)
        else:
            st.error("Failed to generate responses. Please check the input or try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if st.button("Submit"):
    asyncio.run(main())