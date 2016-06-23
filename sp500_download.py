import datetime
import pandas as pd
import pandas.io.data

import urllib

start_date = datetime.datetime(2000, 10, 1)
end_date = datetime.datetime(2016, 12, 31)

sp500 = pd.io.data.get_data_yahoo('%5EGSPC', start=start_date, end=end_date)
print sp500.tail()
sp500.to_csv('sp500.csv')

vix = pd.io.data.get_data_yahoo('%5EVIX', start=start_date, end=end_date)
vix.to_csv('vix.csv')
print vix.tail()

dl_file = urllib.URLopener()
dl_file.retrieve("http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/equitypc.csv", "equitypc.csv")

