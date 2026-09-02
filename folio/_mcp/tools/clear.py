import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "memory", "memory.db")

def clear_memory(key: str = "all"):
    """delete and clear saved data from local memory database, use all to clear everything"""
    try:
        c = sqlite3.connect(DB_PATH)
        if key == "all":
            c.execute("DELETE FROM memory")
            c.commit()
            c.close()
            return {"status": "cleared", "message": "all memory deleted"}
        else:
            c.execute("DELETE FROM memory WHERE key LIKE ?", (f"%{key}%",))
            c.commit()
            c.close()
            return {"status": "cleared", "key": key}
    except Exception as e:
        return f"> Clear memory failed: {str(e)}"
