# Resume Parser

A web-based resume parsing application built with **Flask, spaCy, pdfplumber, and PostgreSQL**. The application accepts PDF resumes, extracts relevant candidate information, and stores the parsed data in a PostgreSQL database.

## 🚀 Live Demo

**Live Application:** https://resume-parser-wf6x.onrender.com

**GitHub Repository:** https://github.com/Ajay-Kumar-0001/resume-parser

> Note: The application is deployed on Render's free tier, so the first request after inactivity may take some time while the service starts.

---

## 📌 Project Overview

The Resume Parser automates the extraction of important information from PDF resumes.

Instead of manually reviewing every resume, a recruiter can upload a PDF and the application extracts information such as:

- Candidate name
- Email address
- Phone number
- Skills
- Education
- Years of experience
- Original resume text

The extracted information is stored in PostgreSQL and displayed through a web interface.

---

## ✨ Features

- 📄 PDF resume upload
- 🔍 Automatic text extraction from PDF files
- 👤 Candidate name extraction using spaCy NER
- 📧 Email extraction using regular expressions
- 📱 Phone number extraction
- 🛠️ Skill detection using keyword matching
- 🎓 Education detection
- 💼 Experience-years extraction
- 🗄️ PostgreSQL database storage
- 📊 Candidate results table
- 🔎 Individual candidate detail view
- 🔗 JSON API endpoint for candidates
- ☁️ Cloud deployment using Render

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Flask | Web framework |
| spaCy | Natural Language Processing and Named Entity Recognition |
| pdfplumber | PDF text extraction |
| PostgreSQL | Database |
| psycopg2 | PostgreSQL connectivity |
| HTML/CSS | Frontend |
| Gunicorn | Production WSGI server |
| Render | Cloud deployment |
| Git & GitHub | Version control |

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    │   Uploads Resume    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask Web App    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     pdfplumber      │
                    │   Extract PDF Text  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       parser.py     │
                    │                     │
                    │  • spaCy NER        │
                    │  • Regex            │
                    │  • Keyword Matching │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │     candidates      │
                    │       table         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Results / Detail  │
                    │       Pages         │
                    └─────────────────────┘

                    ⚙️ How It Works
1. Resume Upload

The user uploads a PDF resume through the Flask web interface.

2. PDF Text Extraction

pdfplumber extracts the raw text from the uploaded PDF.

3. Information Extraction

The extracted text is processed by parser.py.

Different techniques are used for different fields:

spaCy NER → identifies the candidate's name
Regular expressions → extract email, phone number, and experience years
Keyword matching → identifies skills and education mentions
4. Database Storage

The extracted candidate information is stored in PostgreSQL.

5. Results Display

The Flask application displays the parsed candidates in a results table and provides a detail view for individual candidates.

📂 Project Structure
resume_parser/
│
├── app.py                  # Flask application and routes
├── parser.py               # Resume parsing and information extraction
├── db.py                   # PostgreSQL database operations
├── schema.sql              # Database table definition
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .python-version        # Python version used for deployment
│
├── templates/              # HTML templates
│   ├── index.html
│   └── ...
│
└── uploads/                # Uploaded PDF files
💻 Local Installation
1. Clone the repository
git clone https://github.com/Ajay-Kumar-0001/resume-parser.git
cd resume-parser
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment

Windows PowerShell:

venv\Scripts\Activate.ps1

Linux/macOS:

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt

The spaCy language model is included in requirements.txt, so it is installed automatically.

🗄️ Database Configuration

The application uses PostgreSQL.

Create a PostgreSQL database named:

resume_parser

The application uses the DATABASE_URL environment variable for database configuration.

Windows PowerShell example
$env:DATABASE_URL="your_database_connection_string"

The database schema is automatically initialized when the application starts.

▶️ Running the Application Locally

After completing the installation and database setup:

python app.py

The application will be available at:

http://127.0.0.1:5000

Open the URL in a browser and upload a PDF resume.

🔗 API Endpoint

The application also provides a JSON endpoint for retrieving candidate data:

/api/candidates

When running locally:

http://127.0.0.1:5000/api/candidates
☁️ Deployment

The application is deployed on Render using:

Python 3.12
Gunicorn
PostgreSQL
Environment variables for configuration
Production Start Command
gunicorn app:app

The application is connected to a PostgreSQL database hosted on Render.

🔐 Security Notes

Sensitive configuration values such as:

Database credentials
DATABASE_URL
SECRET_KEY

are stored using environment variables and are not committed to the GitHub repository.

Uploaded PDF files are excluded from Git tracking using .gitignore.

🔮 Future Improvements

Possible future enhancements include:

Resume-to-job-description matching using TF-IDF and cosine similarity
Multi-file batch resume processing
CSV/Excel export
Recruiter authentication
Advanced skill extraction
Improved entity recognition
Resume ranking based on job requirements
More comprehensive resume section detection
🎯 Project Purpose

This project was developed as a practical demonstration of:

Python web development
Natural Language Processing
PDF processing
Database integration
REST API development
Cloud deployment
Git/GitHub workflow

**Important:** Paste it exactly as above into `README.md`, save it, and **don't push it yet**. Then tell me **DONE**.