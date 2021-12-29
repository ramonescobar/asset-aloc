import pandas_datareader.data as web
import pandas as pd
import time
from functools import reduce


def get_crypto(coin, start_date, end_date):
    hist = web.DataReader(f"{coin}", "yahoo", start_date, end_date)
    hist[f"{coin}"] = hist["Close"]
    hist = hist[[f'{coin}']]
    return hist

def multiple_stocks(stocks, currency, start_date, end_date):
    time.sleep(3)
    dfs = []
    for c in stocks:
        yc = c + "-" + currency
        dfs.append(get_crypto(yc, start_date, end_date))
    dfm = reduce(lambda left, right: pd.merge(left, right, on=['Date'], how='outer'), dfs)

    return dfm.reset_index()
