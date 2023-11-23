# https://stackoverflow.com/a/77509505/22943567

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web 
import numpy as np
import yfinance as yf
yf.pdr_override()

ticker = "team"
stock = yf.Ticker(ticker)

data = web.get_data_yahoo(ticker, start="2000-1-1", end=dt.datetime.now())
data['100ma'] = data['Adj Close'].rolling(window = 100, min_periods = 0).mean()

print(data)

# data['Close'].plot()
# data['100ma'].plot()

web.get_data_yahoo('team', start="2000-1-1", end=dt.datetime.now())['Close'].plot()
web.get_data_yahoo('aapl', start="2000-1-1", end=dt.datetime.now())['Close'].plot()

plt.show()