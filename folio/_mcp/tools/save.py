from datetime import datetime
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "memory", "memory.db")

def history_db():
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok = True)
        c = sqlite3.connect(DB_PATH)
        c.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT,
                response TEXT,
                saved_at TEXT
            )
        """)

        c.commit()
        c.close()
    except Exception as e:
        return f"> Error in db: {e}"

def save_history(query: str, response: str):
    """Log chat query and response to history database only. NOT for saving files, research, or summaries. Use write_file for that."""
    try:
        history_db()
        c = sqlite3.connect(DB_PATH)
        c.execute("INSERT INTO history (query, response, saved_at) VALUES (?, ?, ?)",
                     (query, response, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        c.commit()
        c.close()
        return {"status": "saved", "query": query}
    except Exception as e:
        return f"> Save history failed: {str(e)}"