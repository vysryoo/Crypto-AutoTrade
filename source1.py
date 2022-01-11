import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-ETH", count=365*3)
df['max'] = df['close'].max()
df['mdd'] = ((df['close'] - df['max'])/df['max'])*100
df.to_excel("data.xlsx")

print(df)
data = df.loc['2022-01-11 09:00:00','mdd']
print(data)