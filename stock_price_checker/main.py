import json
import os
from datetime import datetime, timedelta

import requests

API_KEY = 'cnr8fnpr01qs2jr5mj30cnr8fnpr01qs2jr5mj3g'
BASE_URL = 'https://finnhub.io/api/v1/'
DAYS_BACK = 7
SYMBOL = "YNDX"


def check_price():
    stock = input('Введите абревиатуру акции: ')
    url = f"{BASE_URL}quote?symbol={stock}&token={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    print(f'{stock} = {data['c']} $')

    # params = {
    #     'symbol': SYMBOL,
    #     'resolution': 'D',
    #     'from': int(datetime.timestamp(datetime.now() - timedelta(days=DAYS_BACK))),
    #     'to': int(datetime.timestamp(datetime.now())),
    #     'token': API_KEY
    # }
    # url = f"{BASE_URL}stock/candle"
    # response = requests.get(url, params=params)
    # data_candles = json.loads(response.text)
    # print(data_candles)
    # last_days_back_average = sum(data_candles['c']) / len(data_candles['c'])

    # if data['c'] > last_days_back_average:
    #     print("Цена акции Apple выше средней цены за последние 7 дней")
    # else:
    #     print("Цена акции Apple ниже средней цены за последние 7 дней")


if __name__ == '__main__':
    check_price()
