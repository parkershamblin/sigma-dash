import requests
import pandas as pd
import numpy as np
from datetime import datetime
from time import time
import dateutil.parser

def request_history(symbol, interval_mins=60, load_periods=500):
    
    end_t = int(time()) + 120*interval_mins
    end_t -= end_t % (60*interval_mins)
    start_t = end_t - load_periods*60*interval_mins

    baseurl = 'https://www.bitmex.com/api'
    url = baseurl + f'/udf/history?symbol={symbol}&resolution={interval_mins}&from={start_t}&to={end_t}'
    req = requests.get(url).json()

    df = pd.DataFrame(req)
    # rename headers to something more explicitive
    df.rename({'t': 'date', 'c': 'close', 'o': 'open', 'h': 'high', 'l': 'low', 'v': 'volume'}, axis=1, inplace=True)
    # convert date column from unix to datetime object
    df['date'] = pd.to_datetime(df['date'], origin='unix', unit='s')
    # add colors to customization volume bar chart
    df['color'] = np.where(df['close'] > df['open'], 'green', 'red')

    return df
