from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd


# Getting symbols

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '25',
    'convert': 'USD'
}

if True:
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '795b66e0-7861-4d06-b8fd-fa82d5b154d6',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        data = pd.DataFrame(data['data'])
        data = data[['name', 'symbol']]
        data.to_csv('crypto-currencies.csv')
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pass