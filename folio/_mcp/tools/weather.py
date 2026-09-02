import requests


def _weather(query: str):
    """get current weather, forecast, temperature, humidity, and atmospheric conditions for any city or location"""
    try:
        url = f"https://wttr.in/{query}?format=j1"
        response = requests.get(url)
        data = response.json()
        current = data["current_condition"][0]
        result = (f"""
        🌆  City          : {query}
        🌡️   Temp          : {current["temp_C"]}°C  
        🤔  Feel's Like   : {current["FeelsLikeC"]}°C
        💧  Humidity      : {current["humidity"]}% 
        💨  Wind Speed    : {current["windspeedKmph"]}kmph 
        ☁️   Condition     : {current["weatherDesc"][0]["value"]}
        """)

        return result
    
    except:
        return "> Weather unavailable"
    

