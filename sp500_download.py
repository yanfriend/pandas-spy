import datetime
import pandas as pd
from pandas_datareader import data as web

import urllib

start_date = datetime.datetime(2000, 10, 1)
end_date = datetime.datetime.now()

try:
    sp500 = web.DataReader('^GSPC', 'yahoo', start=start_date, end=end_date)
    print sp500.tail()
    sp500.to_csv('sp500.csv')

    vix = web.DataReader('^VIX', 'yahoo', start=start_date, end=end_date)
    vix.to_csv('vix.csv')
    print vix.tail()
except Exception as e:
    print e

dl_file = urllib.URLopener()
dl_file.retrieve("http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/equitypc.csv", "equitypc.csv")

