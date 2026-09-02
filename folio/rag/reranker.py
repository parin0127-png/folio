from folio.imports import get
class Reranker:
    def __init__(self, embedder):
        self.embedder = embedder

    def rerank(self, query, chunks, top_k = 3):
        np = get("numpy")
        query_emb = self.embedder.embed(query)

        scored = []
        for chunk in chunks:
            chunk_emb = np.array(chunk["embedding"])
            score = np.dot(query_emb, chunk_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(chunk_emb))
            scored.append((score, chunk))


        scored.sort(key = lambda x: x[0], reverse = True)

        scores_only = [s for s, _ in scored]
        threshold = np.mean(scores_only)

        results = []
        for score, chunk in scored:
            if score >= threshold:
                results.append(chunk)

        return results[:top_k]  