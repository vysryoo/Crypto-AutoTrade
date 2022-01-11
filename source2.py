import time
import pyupbit
import datetime
import numpy as np


access = "access-key"          
secret = "secret-key"         
upbit = pyupbit.Upbit(access, secret)

mdd = -85
unit = 10000
crypto = "KRW-ETH"
interval = 60*60*24

def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, count=1)
    start_time = df.index[0]
    return start_time


def get_execution(ticker):
    df = pyupbit.get_ohlcv(ticker, count=365*3)
    df['max'] = df['close'].max()
    df['mdd'] = ((df['close'] - df['max'])/df['max'])*100
    today_mdd = df.loc[get_start_time(ticker), 'mdd']
    if today_mdd < mdd:
        return 1 # 1이면 매수
    else:
        return 0 # 0이면 매수하지 않음        

while True:

    try:
        now = datetime.datetime.now()
        start_time = get_start_time(crypto)
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            if get_execution(crypto) == 1:
                krw = upbit.get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order(crypto, unit)
                    time.sleep(interval)
    except Exception as e:
        print(e)
        time.sleep(1)
