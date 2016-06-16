import datetime
import pandas as pd
import pandas.io.data

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import style

interested_range = -500

# style.use('ggplot')

sp = pd.read_csv('sp500.csv', index_col='Date', parse_dates=True)
sp_close = sp['Adj Close']
sp_close = sp_close[interested_range:]

ax1 = plt.subplot(3,1,1)
ax1.plot(sp_close, label='sp500')
plt.legend(loc='upper left')

vix = pd.read_csv('vix.csv', index_col='Date', parse_dates=True)
vix_close = vix['Adj Close']
vix_close = vix_close[interested_range:]

ax1 = plt.subplot(3,1,2)
ax1.plot(vix_close, label='vix')
plt.legend(loc='upper left')

pcr = pd.read_csv('equitypc.csv', index_col='DATE', parse_dates=True, skiprows=2)
pcr = pcr['P/C Ratio']

ma = pd.rolling_mean(pcr, 13)
ma = ma[interested_range:]

ax2 = plt.subplot(3,1,3, sharex=ax1)
ax2.plot(ma, label='ma')
plt.legend(loc='upper left')


#from matplotlib.widgets import Cursor
#cursor = Cursor(ax1, useblit=True, color='red', linewidth=2 )  # need improve

plt.show()

