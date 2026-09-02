import requests

def get_crypto(query: str):
    """Get live cryptocurrency prices. Use for bitcoin, ethereum, BTC, ETH, crypto price, coin price, digital asset market data, and crypto trading information."""
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={query}&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
        headers = {"User-Agent": "Mozilla/5.0"}
        data = requests.get(url, headers = headers).json()
        info = data[query]

        result = (
            f"""
    🪙   coin         :  {query.upper()} 
    💰  price        :  ${info['usd']},
    📊  market cap   :  ${info['usd_market_cap']:,.0f}
    📈  24h change   :  {info['usd_24h_change']:.2f}%
            """
        )
        return result
    except:
        return "> Crypto data unavailable"
    
