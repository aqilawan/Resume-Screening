# backend/main.py

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from model import ResumeJobMatcher
from utils import extract_text_from_pdf

import uvicorn

# -------------------------------
# INIT APP
# -------------------------------
app = FastAPI(
    title="Resume Job Matching System",
    description="AI-powered resume screening using NLP",
    version="1.0"
)

# Enable CORS (for frontend like Streamlit / React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model once (IMPORTANT for performance)
matcher = ResumeJobMatcher()


# -------------------------------
# HEALTH CHECK
# -------------------------------
@app.get("/")
def home():
    return {
        "message": "Resume Job Matching API is running 🚀"
    }


# -------------------------------
# MAIN ENDPOINT
# -------------------------------
@app.post("/match")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Upload resume + job description → returns match score
    """

    # Step 1: Extract text from PDF
    resume_text = extract_text_from_pdf(resume.file)

    if not resume_text:
        return {
            "error": "Could not extract text from resume"
        }

    # Step 2: Compute similarity score
    score = matcher.get_match_score(resume_text, job_description)

    # Step 3: Response
    return {
        "filename": resume.filename,
        "match_score": score,
        "status": "success"
    }


# -------------------------------
# RUN SERVER (LOCAL TESTING)
# -------------------------------
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )