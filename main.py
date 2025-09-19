import requests
import time
from datetime import datetime as dt

def get_btc_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=thb,usd'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_thb = data['bitcoin']['thb']
        price_usd = data['bitcoin']['usd']
        return price_thb, price_usd, 200
    else:
        if response.status_code == 429:
            print("Rate limit exceeded")
        else:
            print(f"Error fetching data: {response.status_code}")
        return None, None, response.status_code
    
while True:
    thb, usd, status_code = get_btc_price()
    time_stamp = dt.now().strftime('%Y-%m-%d %H:%M:%S')

    if thb and usd:
        print(f"[{time_stamp}] Bitcoin price: {thb:,} THB | {usd} USD")
    else:
        print(f"[{time_stamp}] Failed to retrieve price.")

    time.sleep(5)

    if status_code == 429:
        print("Rate limit exceeded. Exiting loop")
        break