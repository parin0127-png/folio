import requests

def check_status(url: str):
    """check if any website or url is currently online, offline, or down"""
    try:
        res = requests.get(url)
        return {
            "url" : url,
            "status": "online" if res.status_code == 200 else "Issue",
            "code" : res.status_code
        }
    except Exception as e:
        return {"url": url, "status": "offline"}

