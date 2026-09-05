import re
import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"(\+?\d{1,3}[-.\s]?)?\(?\d{3,4}\)?[-.\s]?\d{3}[-.\s]?\d{3,4}")

SKILL_DB = [
    "python", "java", "c++", "c", "javascript", "typescript", "react", "node.js",
    "flask", "django", "spring", "sql", "postgresql", "mysql", "mongodb",
    "machine learning", "deep learning", "nlp", "spacy", "tensorflow", "pytorch",
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "html", "css",
    "data analysis", "pandas", "numpy", "excel", "power bi", "tableau",
    "rest api", "microservices", "linux", "agile", "scrum",
]

EDU_KEYWORDS = ["b.tech", "btech", "bachelor", "m.tech", "mtech", "master",
                "b.sc", "m.sc", "phd", "diploma", "university", "college", "institute"]


def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_name(doc, text):
    # Prefer first PERSON entity found near top of resume
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip()
    # fallback: first non-empty line
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line
    return None


def extract_email(text):
    m = EMAIL_RE.search(text)
    return m.group(0) if m else None


def extract_phone(text):
    m = PHONE_RE.search(text)
    return m.group(0).strip() if m else None


def extract_skills(text):
    lower = text.lower()
    found = [s for s in SKILL_DB if s in lower]
    return sorted(set(found))


def extract_education(text):
    lines = text.splitlines()
    found = []
    for line in lines:
        low = line.lower()
        if any(kw in low for kw in EDU_KEYWORDS):
            found.append(line.strip())
    return found[:5]


def extract_experience_years(text):
    m = re.search(r"(\d+(\.\d+)?)\s*\+?\s*years?", text.lower())
    if m:
        return float(m.group(1))
    return None


def parse_resume(pdf_path, filename):
    text = extract_text(pdf_path)
    doc = nlp(text[:100000])  # cap for very large docs

    return {
        "filename": filename,
        "name": extract_name(doc, text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience_years": extract_experience_years(text),
        "raw_text": text,
    }
