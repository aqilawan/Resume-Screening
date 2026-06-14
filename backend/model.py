# backend/model.py

from sentence_transformers import SentenceTransformer, util
from utils import clean_text


class ResumeJobMatcher:
    """
    Semantic Resume-Job Matching using SentenceTransformer embeddings.
    """

    def __init__(self):
        # Lightweight, fast, production-friendly model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    # -------------------------------
    # MAIN MATCHING FUNCTION
    # -------------------------------
    def get_match_score(self, resume_text, job_text):
        """
        Compute semantic similarity score between resume and job description.

        Args:
            resume_text (str)
            job_text (str)

        Returns:
            float: similarity score (0 - 100)
        """

        # Step 1: Clean input text
        resume_text = clean_text(resume_text)
        job_text = clean_text(job_text)

        # Step 2: Encode texts into embeddings
        resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
        job_embedding = self.model.encode(job_text, convert_to_tensor=True)

        # Step 3: Compute cosine similarity
        similarity_score = util.cos_sim(resume_embedding, job_embedding)

        # Step 4: Convert to percentage
        score = float(similarity_score.item()) * 100

        return round(score, 2)