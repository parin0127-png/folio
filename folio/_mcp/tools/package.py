import requests

def packages_info(package_name: str):
    "lookup PyPI package metadata such as version and package description"
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)
        data = response.json()["info"]

        return {
            "name" : data["name"],
            "version": data["version"],
            "description": data["summary"],
            "author" : data.get("author") or data.get("author_email") or data.get("maintainer") or "N/A",
            "url": data["project_url"]
        }
    except Exception as e:
        return f"> Package info failed: {str(e)}"

