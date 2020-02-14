import urllib.request
import requests
import json


exchange_SECRET_KEY="CQJZGTj2RAQYrW61ldyW2PYU4MPhBzKM"
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=CQJZGTj2RAQYrW61ldyW2PYU4MPhBzKM&searchdate=20200212&data=AP01'
exchange = requests.get(url).json()

for info in exchange:
    if info['cur_unit']=='USD':
        print(info['ttb'])


exchange_total = info['ttb'] * total
accumulate += exchange_total

