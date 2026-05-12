import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Resume Tailor")

st.title("AI Resume Tailor App")

st.write("Upload resume and tailor it for a job description")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description"
)

job_url = st.text_input(
    "OR Paste Job URL"
)

if st.button("Generate Tailored Resume"):

    if uploaded_file:

        files = {
            "resume": (
                uploaded_file.name,
                uploaded_file,
                uploaded_file.type
            )
        }

        data = {
            "job_description": job_description,
            "job_url": job_url
        }

        with st.spinner("Generating Resume..."):

            response = requests.post(
                f"{BACKEND_URL}/generate-resume",
                files=files,
                data=data
            )

        if response.status_code == 200:

            result = response.json()

            st.success("Resume Generated Successfully")

            st.subheader("Extracted Keywords")
            st.write(result["keywords"])

            download_url = (
                BACKEND_URL + result["download_url"]
            st.error("Something went wrong")
            )