from folio._mcp.tools.websearch import web_search
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def search_visa_info(from_country: str, to_country: str):
    """find visa requirements, travel permits, and entry information between any two countries"""
    try:
        return web_search(f"visa requirements for {from_country} citizens visiting {to_country}")
    except Exception as e:
        return f"> Visa info failed: {str(e)}"

