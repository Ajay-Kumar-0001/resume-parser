CREATE TABLE IF NOT EXISTS candidates (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    name TEXT,
    email TEXT,
    phone TEXT,
    skills TEXT[],
    education TEXT[],
    experience_years FLOAT,
    raw_text TEXT,
    uploaded_at TIMESTAMP DEFAULT NOW()
);
