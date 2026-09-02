from datetime import date
import requests

def score(sport: str):
    """get live and recent sports scores, match results, fixtures, and game updates"""
    try:
        today = date.today().strftime("%Y-%m-%d")
        url = f"https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d={today}&s={sport}"
        response = requests.get(url, timeout = 5)
        data = response.json()

        events = data.get("events", [])
        output = []
        for e in events[:5]:
            output.append({
                "match": f"{e.get('strHomeTeam')} vs {e.get('strAwayTeam')}",
                "score": f"{e.get('intHomeScore')} - {e.get('intAwayScore')}",
                "date": e.get("dateEvent")
            })
        return output
    except Exception as e:
        return f"> Sports scores failed: {str(e)}"

