import sys
sys.path.append("C:\\Users\\Parin\\OneDrive\\Desktop\\FOLIO")

from folio.config import search_client
from ddgs import DDGS

def web_search(query: str, max_result = 5):
    """search the web for information, research, competitor analysis, news, facts, and any online query"""
    try:
        browser = search_client.search(query, max_results = max_result)
        results = []

        if not browser.get("results"):
            return "> Please try again !"
        
        for r in browser["results"]:
            results.append({
                "title" : r["title"],
                "url" : r["url"],
                "content" : r["content"]
            })
        
        return results
    except:
        results = []
        for r in DDGS().text(query, max_results = max_result):
            results.append({
                "title" : r["title"],
                "url" : r["href"],
                "content" : r["body"]
            })
        return results