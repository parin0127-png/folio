import wikipediaapi

def wikipedia_search(query):
    """search wikipedia for summaries, facts, biography, and information about any topic or person"""
    try:
        wiki = wikipediaapi.Wikipedia(user_agent = "FOLIO/1.0", language = "en")
        page = wiki.page(query) 

        if not page.exists():
            return "> Wikipedia : page not found"

        result = f"""
                📖 Title    : {page.title}
                📝 Summary  : {page.summary[:500]}
                🔗 Url      : {page.fullurl}
            """
        return f"{page.title}\n{page.summary[:1200]}"
    except:
        return "> Wikipedia : data is unavailable."
