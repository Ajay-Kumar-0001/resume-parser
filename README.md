# Resume Parser (Flask + spaCy + pdfplumber + PostgreSQL)

## Setup
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Database
1. Create a PostgreSQL database named `resume_parser` (or set `DATABASE_URL` env var).
2. Schema is auto-created on first run (`schema.sql` via `db.init_db()`).

Example:
```bash
createdb resume_parser
export DATABASE_URL="dbname=resume_parser user=postgres password=postgres host=localhost port=5432"
```

## Run
```bash
python app.py
```
Visit http://127.0.0.1:5000 — upload a PDF resume, it's parsed and stored, and results show in a table with a detail view per candidate.

## How it works
- **pdfplumber** extracts raw text from the uploaded PDF.
- **spaCy** (`en_core_web_sm`) runs NER to detect the candidate's name (PERSON entity).
- **Regex** extracts email and phone number.
- A keyword list matches known **skills** and **education** mentions; years of experience is regex-matched (e.g. "3+ years").
- **PostgreSQL** stores each parsed candidate; Flask serves the upload form, results table, and per-candidate detail page, plus a `/api/candidates` JSON endpoint.

## Project structure
```
app.py          - Flask routes
parser.py       - pdfplumber + spaCy extraction logic
db.py           - PostgreSQL access layer
schema.sql      - table definition
templates/      - HTML pages
uploads/        - saved PDF resumes
```

## Possible extensions (for report/demo)
- Resume-to-job-description matching score (TF-IDF/cosine similarity)
- Multi-file batch upload
- Export results to CSV/Excel
- Authentication for recruiter accounts
