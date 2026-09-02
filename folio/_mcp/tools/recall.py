import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "memory", "memory.db")
def recalls(key: str):
    """search and retrieve any previously saved information or notes from local memory database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c= conn.execute("SELECT key, value, saved_at FROM memory WHERE key LIKE ?", (f"%{key}%",))
        rows = c.fetchall() 
        conn.close()

        if not rows:
            return {"Status": "Not found", "Key": key}

        result = [{"Key": r[0], "Value": r[1], "saved_at": r[2]} for r in rows]
        return {"Status": "found", "results": result}
    except Exception as e:
        return f"> Recall failed: {str(e)}"

