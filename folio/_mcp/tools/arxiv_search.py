import arxiv

def _arxiv_search(query: str, max_result = 5):
    """search arxiv for academic research papers, scientific studies, and articles on any topic"""
    try:
        client = arxiv.Client()
        search = arxiv.Search(query, max_results = max_result)
        results = client.results(search)

        outputs = []
        for paper in results:
            outputs.append({
                "title": paper.title,
                "author": [a.name for a in paper.authors[:3]],
                "summary": paper.summary[:2500],
                "url": paper.entry_id
            })
        return outputs
    except Exception as e:
        return f"> Arxiv search failed: {str(e)}"
