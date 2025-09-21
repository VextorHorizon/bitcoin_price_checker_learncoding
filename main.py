import requests
import time
from datetime import datetime as dt

def get_coin_price():
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=thb,usd'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if coin in data:
            price_thb = data[coin]['thb']
            price_usd = data[coin]['usd']
            return price_thb, price_usd, 200, coin
        else:
            print(f"Coin ID '{coin}' not found in response.")
            return None, None, 404
    else:
        if response.status_code == 429:
            print("Rate limit exceeded")
        else:
            print(f"Error fetching data: {response.status_code}")
        return None, None, response.status_code, 'N/A'

coin = input("Your coins id(bitcoin,ethereum,dogecoin): ").strip().lower()

while True:
    thb, usd, status_code, coin = get_coin_price()
    time_stamp = dt.now().strftime('%Y-%m-%d %H:%M:%S')

    if thb and usd:
        print(f"[{time_stamp}] {coin} price: {thb:,} THB | {usd} USD")
    else:
        print(f"[{time_stamp}] Failed to retrieve price.")

    time.sleep(5)

    if status_code == 429:
        ask = input("Do you want to continues?(y/n): ").strip().lower()
        if ask == 'y':
            continue
        if ask == 'n':
            exit()
        else:
            print("(y/n only!)")
            continue
