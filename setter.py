from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2019-05-26')
secDpc = (sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
#NaN = 0
secDpc.iloc[0] = 0
secDpcCp = ((100 + secDpc) / 100).cumprod() * 100 - 100

MSFT = pdr.get_data_yahoo('MSFT', start='2019-05-26')
MSFTDpc = (MSFT['Close'] / MSFT['Close'].shift(1) - 1) * 100
MSFTDpc.iloc[0] = 0
MSFTDpcCp = ((100 + MSFTDpc) / 100).cumprod() * 100 - 100

plt.plot(sec.index, secDpcCp, 'b', label='Samsung Electronics')
plt.plot(MSFT.index, MSFTDpcCp, 'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()