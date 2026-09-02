from folio._mcp.tools.websearch import web_search
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def search_product(query: str):
    """searches for products prices and shopping deals online"""
    try:
        return web_search(f"{query} buy online price site:amazon.in OR site:flipkart.com")
    except Exception as e:
        return f"> Product search failed: {str(e)}"

