import sqlite3, json

class VectorStore:
    def __init__(self, db_path="rag_db"):
        self.conn = sqlite3.connect(f"{db_path}.sqlite", check_same_thread=False)
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS chunks (
                chunk_id TEXT PRIMARY KEY, text TEXT, embedding TEXT, source TEXT
            );
            CREATE TABLE IF NOT EXISTS edges (
                from_id TEXT, to_id TEXT, relation TEXT,
                PRIMARY KEY (from_id, to_id, relation)
            );
        """)

    def add(self, chunks, embeddings):
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
            cid = f"{chunk['source']}_{chunk['index']}"
            self.conn.execute("INSERT OR REPLACE INTO chunks VALUES (?,?,?,?)",
                (cid, chunk["text"], json.dumps(emb.tolist()), chunk["source"]))
            if i > 0:
                prev = f"{chunks[i-1]['source']}_{chunks[i-1]['index']}"
                self.conn.execute("INSERT OR IGNORE INTO edges VALUES (?,?,?)", (prev, cid, "next"))
        self.conn.commit()

    def get_all(self):
        rows = self.conn.execute("SELECT chunk_id, text, embedding, source FROM chunks").fetchall()
        return [{"chunk_id": r[0], "text": r[1], "embedding": json.loads(r[2]), "source": r[3]} for r in rows]

    def get_neighbors(self, chunk_id, relation=None):
        if relation:
            rows = self.conn.execute("SELECT to_id FROM edges WHERE from_id=? AND relation=?", (chunk_id, relation)).fetchall()
        else:
            rows = self.conn.execute("SELECT to_id FROM edges WHERE from_id=?", (chunk_id,)).fetchall()
        if not rows:
            return []
        ids = [r[0] for r in rows]
        result = self.conn.execute(f"SELECT chunk_id, text, embedding, source FROM chunks WHERE chunk_id IN ({','.join('?'*len(ids))})", ids).fetchall()
        return [{"chunk_id": r[0], "text": r[1], "embedding": json.loads(r[2]), "source": r[3]} for r in result]

    def add_edge(self, from_id, to_id, relation="related"):
        self.conn.execute("INSERT OR IGNORE INTO edges VALUES (?,?,?)", (from_id, to_id, relation))
        self.conn.commit()

    def get_graph(self):
        rows = self.conn.execute("SELECT from_id, to_id, relation FROM edges").fetchall()
        return [{"from": r[0], "to": r[1], "relation": r[2]} for r in rows]