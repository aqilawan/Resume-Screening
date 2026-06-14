# frontend/app.py

import streamlit as st
import requests

# -------------------------------
# CONFIG
# -------------------------------
API_URL = "http://127.0.0.1:8000/match"

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(
    page_title="Resume Job Matcher",
    page_icon="📄",
    layout="centered"
)

# -------------------------------
# HEADER
# -------------------------------
st.title("📄 AI Resume Job Matching System")
st.write(
    "Upload your resume and paste a job description to see how well they match."
)

# -------------------------------
# FILE UPLOAD
# -------------------------------
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -------------------------------
# JOB DESCRIPTION INPUT
# -------------------------------
job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# -------------------------------
# MATCH BUTTON
# -------------------------------
if st.button("Match Resume"):
    
    if resume_file is None:
        st.warning("Please upload a resume.")
    
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    
    else:
        try:
            with st.spinner("Analyzing resume..."):

                files = {
                    "resume": (
                        resume_file.name,
                        resume_file,
                        "application/pdf"
                    )
                }

                data = {
                    "job_description": job_description
                }

                response = requests.post(
                    API_URL,
                    files=files,
                    data=data
                )

                if response.status_code == 200:

                    result = response.json()

                    score = result["match_score"]

                    st.success("Analysis Complete ✅")

                    st.metric(
                        label="Match Score",
                        value=f"{score}%"
                    )

                    # Optional score interpretation
                    if score >= 80:
                        st.success("Excellent Match 🎯")

                    elif score >= 60:
                        st.info("Good Match 👍")

                    elif score >= 40:
                        st.warning("Moderate Match ⚠️")

                    else:
                        st.error("Low Match ❌")

                else:
                    st.error("API Error")

        except Exception as e:
            st.error(f"Connection Error: {e}")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built with Streamlit + FastAPI + SentenceTransformers")