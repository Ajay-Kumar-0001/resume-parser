import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_URL = os.getenv("DATABASE_URL", "dbname=resume_parser user=postgres password=postgres host=localhost port=5432")

def get_conn():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

def init_db():
    conn = get_conn()
    with conn.cursor() as cur:
        with open(os.path.join(os.path.dirname(__file__), "schema.sql")) as f:
            cur.execute(f.read())
    conn.commit()
    conn.close()

def insert_candidate(data):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO candidates (filename, name, email, phone, skills, education, experience_years, raw_text)
            VALUES (%(filename)s, %(name)s, %(email)s, %(phone)s, %(skills)s, %(education)s, %(experience_years)s, %(raw_text)s)
            RETURNING id
        """, data)
        new_id = cur.fetchone()["id"]
    conn.commit()
    conn.close()
    return new_id

def get_all_candidates():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT id, filename, name, email, phone, skills, education, experience_years, uploaded_at FROM candidates ORDER BY uploaded_at DESC")
        rows = cur.fetchall()
    conn.close()
    return rows

def get_candidate(cid):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM candidates WHERE id = %s", (cid,))
        row = cur.fetchone()
    conn.close()
    return row
