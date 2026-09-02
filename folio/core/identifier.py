from folio.core.cache_manager import load
from folio.imports import get


_cache = None
def get_cache():
    global _cache
    if _cache is None:
        _cache = load()
    return _cache


def extract_tool(task: str, top_k: int = 15):
    try:
        _cache = get_cache()
        _tool_names = _cache["tool_names"]
        _tool_dict = _cache["tool_dict"]
        _tool_embd = _cache["tool_embd"]

        n = get("numpy")
        cosine_similarity = get("cosine_similarity")
        
        task_embd = get("sentence_transformer").encode([task])
        
        scores = cosine_similarity(task_embd, _tool_embd)[0]

        top = n.argsort(scores)[::-1][:top_k]

        candidates = []
        for i in top:
            candidates.append({
                "tool": _tool_names[i],
                "description": _tool_dict[_tool_names[i]],
                "score": float(scores[i])
            })
        return candidates
    
    except Exception as e:
        return f"> Error in creating matrix: {e}"