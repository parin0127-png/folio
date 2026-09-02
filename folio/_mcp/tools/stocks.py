import yfinance as y

def get_stocks(query: str):
    """get real time stock prices, equity data, market performance, and financial information for any company"""
    try:
        stock = y.Ticker(query)
        info = stock.fast_info
        result = f"""
            📈 ticker  : {query.upper()}
            💰 price   : {round(info.last_price, 2)}
            📊 high    : {round(info.day_high, 2)}
            📉 low     : {round(info.day_low, 2)}
            📦 volume  : {info.last_volume}  
        """
        return result
    except:
        return "> Stock unavailable"
    
