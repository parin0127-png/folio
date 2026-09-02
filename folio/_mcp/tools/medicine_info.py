import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  folio._mcp.tools.websearch import web_search

def info_medicine(medicine_name: str):
    """search for medicine information, drug dosage, side effects, and medical usage"""
    try:
        return web_search(f"{medicine_name} medicine uses dosage side effects site:drugs.com OR site:webmd.com")
    except Exception as e:
        return f"> Medicine info failed: {str(e)}"
