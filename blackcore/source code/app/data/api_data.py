import requests
import pandas as pd

def fetch_commodity_data():
    # Example API call to fetch commodity data
    url = "https://api.example.com/commodities"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame()
