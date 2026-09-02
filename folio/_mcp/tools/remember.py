from datetime import datetime
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), ".." , "memory", "memory.db")

def db_con():
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok = True)
        c = sqlite3.connect(DB_PATH)
        c.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT,
                value TEXT,
                saved_at TEXT
            )
        """)

        c.commit()
        c.close()
    except Exception as e:
        return f"> Error to connect with database. {str(e)}"


def remembers(key: str, value: str):
    """permanently save any information, note, or data to local memory database for future use"""
    try:
        db_con()
        c = sqlite3.connect(DB_PATH)
        c.execute("INSERT INTO memory (key, value, saved_at) VALUES (?, ?, ?)",
                  (key, value, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        c.commit()
        c.close()
        return {"Status": "saved", "Key": key, "Value": value}
    except Exception as e:
        return f"> Remember failed: {str(e)}"

