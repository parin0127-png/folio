import http.client
import json, os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("RAPIDAPI_KEY")
def search_hotels(city):
    """find and compare cheapest hotels with ratings, amenities, and booking details for any location"""
    try:
        c = http.client.HTTPSConnection("booking-com.p.rapidapi.com")

        headers = {
        'x-rapidapi-key':KEY ,
        'x-rapidapi-host': "booking-com.p.rapidapi.com"
        }

        c.request("GET", f"/v1/hotels/locations?name={city}&locale=en-gb", headers=headers)
        res = c.getresponse()
        location = json.loads(res.read().decode("utf-8"))

        dest_id = location[0]['dest_id']
        dest_type = location[0]['dest_type']

        c.request("GET", f"/v1/hotels/search?dest_id={dest_id}&dest_type={dest_type}&checkin_date=2026-09-01&checkout_date=2026-09-02&adults_number=1&locale=en-gb&currency=USD&order_by=popularity&filter_by_currency=USD&units=metric&room_number=1", headers=headers)

        res = c.getresponse()
        hotels = json.loads(res.read().decode("utf-8"))
        
        for i, hotel in enumerate(hotels['result'][:5], 1):
            print(f"> Hotel {i}")
            print(f"    Name   : {hotel.get('hotel_name', 'N/A')}")
            print(f"    Price  : {hotel.get('min_total_price', 'N/A')} {hotel.get('currency_code', '')}")
            print(f"    Rating : {hotel.get('review_score', 'N/A')}")
            print("-" * 40)
    except Exception as e:
        return f"> Hotel search failed: {e}"

