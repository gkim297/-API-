import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from scipy import stats
import matplotlib.pylab as plt

yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2001-09-14')
kospi = pdr.get_data_yahoo('^KS11', '2001-09-14')

df = pd.DataFrame({'X':dow['Close'], 'Y':kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

regression = stats.linregress(df.X, df.Y)
regresLine = f'Y = {regression.slope:2f}  X + {regression.intercept:2f}'

plt.figure(figsize=(7,7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regression.slope * df.X + regression.intercept, 'r')
plt.legend(['DOW x KOSPI', regresLine])
plt.title(f'DOW x KOSPI (R = {regression.rvalue:2f})')
plt.xlabel('DOW Jones Industrial Average')
plt.ylabel('KOSPI 지수')
plt.show()