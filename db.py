import sqlite3
from datetime import datetime

DB_PATH = "phishing_analysis.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_text TEXT NOT NULL,
            prediction INTEGER NOT NULL,
            confidence REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phishing_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_text TEXT NOT NULL,
            confidence REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_analysis(email_text, prediction, confidence):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    ts = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO analyses (email_text, prediction, confidence, timestamp) VALUES (?, ?, ?, ?)
    ''', (email_text, prediction, confidence, ts))
    conn.commit()
    conn.close()

def save_phishing_attempt(email_text, confidence):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    ts = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO phishing_attempts (email_text, confidence, timestamp) VALUES (?, ?, ?)
    ''', (email_text, confidence, ts))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    total = cursor.execute("SELECT COUNT(*) FROM analyses").fetchone()[0]
    phishing = cursor.execute("SELECT COUNT(*) FROM phishing_attempts").fetchone()[0]

    conn.close()
    return {"total_analyses": total, "phishing_attempts": phishing}
