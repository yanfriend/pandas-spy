import datetime
import pandas as pd
import pandas.io.data

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


interested_range = -500

# style.use('ggplot')

sp = pd.read_csv('sp500.csv', index_col='Date', parse_dates=True)
sp_close = sp['Adj Close']
sp_close = sp_close[interested_range:]

sp_close = np.log(sp_close / sp_close.shift(1))
print sp_close.tail()

#ax1 = plt.subplot(3,1,1)
#ax1.yaxis.tick_right()
#ax1.plot(sp_close, label='sp500')
#plt.legend(loc='upper left')

vix = pd.read_csv('vix.csv', index_col='Date', parse_dates=True)
vix_close = vix['Adj Close']
vix_close = vix_close[interested_range:]

vix_close = np.log(vix_close / vix_close.shift(1)) # log, normalized
print vix_close.tail()

# finish reading data so far.

xdat = vix_close.shift(20)  # shift forward, so that today's sp close corresponds to x day earlier vix data.  
# 5, 50 -> positive, 15 is best one. 20 is negative, but generally, useless.

print xdat

ydat = sp_close

model = pd.ols(y=ydat, x=xdat)
print model.beta

plt.plot(xdat, ydat, 'r.')

ax = plt.axis()
x = np.linspace(ax[0], ax[1]+0.01)
plt.plot(x, model.beta[1] + model.beta[0]*x, 'b', lw=2)
plt.axis('tight')
plt.show()


# todo 2, use log, normalized 




#ax2 = plt.subplot(3,1,2)
#ax2.yaxis.tick_right()
#ax2.plot(vix_close, label='vix')
#plt.legend(loc='upper left')

#pcr = pd.read_csv('equitypc.csv', index_col='DATE', parse_dates=True, skiprows=2)
#pcr = pcr['P/C Ratio']
#print pcr.tail(13)

#ma = pd.rolling_mean(pcr, 13)
#ma = ma[interested_range:]

#ax3 = plt.subplot(3,1,3, sharex=ax1)
#ax3.yaxis.tick_right()
#ax3.plot(ma, label='pcr ma')
#plt.legend(loc='upper left')

#plt.show()

