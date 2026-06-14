# Resume Job Matching System (AI-powered)

An AI-powered web application that matches resumes with job descriptions using NLP and Sentence Transformers (`all-MiniLM-L6-v2`).  
It computes semantic similarity between resume content and job requirements and returns a **match score (0–100%)**.

---

# Demo

- Upload a resume (PDF)
- Paste a job description
- Get AI-powered match score instantly

---

# Tech Stack

## Backend
- FastAPI
- SentenceTransformers (`all-MiniLM-L6-v2`)
- PyTorch (under the hood)
- Uvicorn

## Frontend
- Streamlit
- Requests

## NLP / ML
- Sentence Embeddings
- Cosine Similarity
