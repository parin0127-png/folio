import requests

def convert_currency(amount: float, from_currency: str, to_currency: str):
    """convert money from one currency to another using live real time exchange rates"""
    try:
        url = f"https://api.frankfurter.app/latest"
        params = {
            "amount": amount,
            "from": from_currency.upper(),
            "to": to_currency.upper()
        }
        data = requests.get(url, params = params).json()
        result = data["rates"][to_currency.upper()]
        return{
            "from": f"{amount} {from_currency.upper()}",
            "to" : f"{result: .2f} {to_currency}"
        }
    except Exception as e:
        return f"> Currency convert failed: {str(e)}"
