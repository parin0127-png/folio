from stackapi import StackAPI

def stack_search(query: str):
    """search stackoverflow for programming questions, code solutions, and developer answers"""
    try:
        site = StackAPI("stackoverflow")
        results = site.fetch("search", intitle = query, sort = "votes")
        output = []
        for q in results["items"][:5]:
            output.append({
                "title" : q["title"],
                "score": q["score"],
                "answered" : q["is_answered"],
                "url": q["link"]
            })
        return output
    except Exception as e:
        return f"> StackOverflow search failed: {str(e)}"
