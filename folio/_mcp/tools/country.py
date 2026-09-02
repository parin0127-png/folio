from countryinfo import CountryInfo

def country_info(query: str):
    """get detailed information about any country including capital, population, currency, and geography"""
    try:
        data = CountryInfo(query)
        return (
            f"🌍  Country: {query}\n"
            f"🏛️  Capital: {data.capital()}\n"
            f"👥  Population: {data.population():,}\n"
            f"💰  Currency: {', '.join(data.currencies())}\n"
            f"🗣️  Languages: {', '.join(data.languages())}\n"
            f"📐  Area: {data.area():,} km²"
        )
    except Exception as e:
        return f"> Country info failed: {str(e)}"

