from fast_flights import Passengers, get_flights, FlightQuery, create_query

def search_flights(origin, destination, date):
    """find and compare the cheapest flights between two airports on a given date"""
    
    try:
        query = create_query(
            flights = [FlightQuery(date = date, from_airport = origin, to_airport = destination)],
            seat = "economy",
            trip = "one-way",
            passengers = Passengers(adults = 1)
        )

        results = get_flights(query)

        seen = set()
        unique = []
        for f in results:
            airlines = f.airlines[0]
            if airlines not in seen:
                seen.add(airlines)
                unique.append(f)
        
        results = unique[:5]
        for i , f in enumerate(results , 1):
            print(f"> Flights {i}")
            print(f"Airlines : {f.airlines}")
            print(f"Price    : {f.price}")

            for leg in f.flights:
                print(f"{leg.from_airport.code} → {leg.to_airport.code}")
                print(f"  Departure : {leg.departure}")
                print(f"  Arrival   : {leg.arrival}")
                print(f"  Duration  : {leg.duration} mins")
                print(f"  Plane     : {leg.plane_type}")
                print("-" * 30)
    except Exception as e:
        return f"> Flight search failed : {e}"

