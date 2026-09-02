import requests

def ip_check(query: str = ""):
    """lookup location, country, ISP, and details about any ip address"""
    try:
        url = f"https://ipinfo.io/{query}/json" if query else "https://ipinfo.io/json"
        data = requests.get(url).json()
        return (
            f"🌐   IP Address: {data.get('ip')}\n"
            f"🏙️   City: {data.get('city')}\n"
            f"📍   Region: {data.get('region')}\n"
            f"🌍   Country: {data.get('country')}\n"
            f"🏢   Organization: {data.get('org')}"
        )
    except Exception as e:
        return f"> IP lookup failed: {str(e)}"
