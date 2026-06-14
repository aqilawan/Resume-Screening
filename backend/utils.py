# backend/utils.py

import re
import PyPDF2


# -------------------------------
# 1. PDF TEXT EXTRACTION
# -------------------------------
def extract_text_from_pdf(pdf_file):
    """
    Extract text from uploaded PDF resume.

    Args:
        pdf_file: file object (uploaded PDF)

    Returns:
        str: extracted text
    """

    text = ""

    try:
        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    except Exception as e:
        print(f"[ERROR] PDF reading failed: {e}")

    return text.strip()


# -------------------------------
# 2. TEXT CLEANING
# -------------------------------
def clean_text(text):
    """
    Clean raw text for NLP processing.

    Steps:
    - lowercase
    - remove URLs
    - remove emails
    - remove phone numbers
    - remove special characters
    - remove extra spaces
    """

    if not text:
        return ""

    # lowercase
    text = text.lower()

    # remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove emails
    text = re.sub(r"\S+@\S+", "", text)

    # remove phone numbers
    text = re.sub(r"\+?\d[\d\s\-()]{7,}", "", text)

    # remove punctuation & special chars
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


# -------------------------------
# 3. OPTIONAL: BASIC KEYWORD EXTRACTION
# -------------------------------
def extract_keywords(text):
    """
    Simple keyword extraction (can be improved later with spaCy).

    Returns:
        list of words
    """

    text = clean_text(text)

    words = text.split()

    # remove very short words
    keywords = [w for w in words if len(w) > 2]

    return list(set(keywords))


# -------------------------------
# 4. OPTIONAL: TEXT LENGTH CHECK
# -------------------------------
def validate_text(text, min_length=20):
    """
    Ensure text is valid enough for processing.

    Returns:
        bool
    """

    if not text:
        return False

    return len(text.strip()) >= min_length