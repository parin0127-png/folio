from rapidfuzz import fuzz
from folio._mcp.client import get_tool_dict
from folio.core.identifier import extract_tool

def get_fuzz_score(task, tool_name, description):
    task = task.lower().replace("_", " ")
    tool_name = tool_name.lower().replace("_", " ")
    description = description.lower()

    tool_score = fuzz.token_set_ratio(task, tool_name)
    desc_score = fuzz.token_set_ratio(task, description)

    return max(tool_score, desc_score)/100

def match_tool(task):
    candidates = extract_tool(task, top_k = len(get_tool_dict()))

    if isinstance(candidates, str):
        return{
            "status": "error",
            "candidate": []
        }

    tool_dict = get_tool_dict()
    results = []

    for candidate in candidates:
        tool_name = candidate["tool"]

        description = tool_dict.get(tool_name,
            candidate["description"])
        
        cosine_score = candidate["score"]

        fuzz_score = get_fuzz_score(task, tool_name, description)

        final_score = (cosine_score * 0.6) + (fuzz_score * 0.4)

        results.append({
            "tool": tool_name,
            "description": description,
            "cosine_score": round(cosine_score, 3),
            "fuzz_score": round(fuzz_score, 3),
            "score": round(final_score, 3)
        })

    results.sort(key = lambda x : x["score"], reverse = True)

    results = results[:2]

    if not results or results[0]["score"] < 0.35:
        return {
            "status": "unresolvable",
            "candidates": results
        }

    return {
        "status": "matched",
        "candidates": results
    }