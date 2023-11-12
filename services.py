import requests


def get_curr():
    """
    Function to get currencies dependecies
    """
    try:
        response = requests.get(url="https://api.exchangerate-api.com/v4/latest/USD")
        if response.status_code == 200:
            curr = response.json().get("rates", None)
            return curr
        else:
            return None
    except:
        return None


def convert(to_curr, from_curr, to_amount, curr):
    """
    Function that converts currencies
    """
    try:
        result = round(((curr[to_curr] / curr[from_curr]) * float(to_amount)), 2)
        return result
    except:
        return None