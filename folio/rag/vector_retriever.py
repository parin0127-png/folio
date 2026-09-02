from folio.imports import get
class VectorRetriever:
    def __init__(self, chunks, embedder):
        np = get("numpy")
        self.chunks = chunks
        self.embedder = embedder
        self.embeddings = np.array([chunk["embedding"] for chunk in chunks])

    def search(self, query, k = 5):
        np = get("numpy")
        query_emb = self.embedder.embed(query)
        scores = np.dot(self.embeddings, query_emb)
        top_k = np.argsort(scores)[::-1][:k]
        return [self.chunks[i] for i in top_k]

    