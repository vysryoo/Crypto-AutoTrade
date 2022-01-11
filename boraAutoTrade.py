import pyupbit
import datetime
import time

def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    k = 0.5

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday['high'] - yesterday['low'])*k
    return target

def buy_crypto_currency(ticker):
    krw = upbit.get_balance(ticker)[2]
    # 보유 중인 원화를 얻어옴
    orderbook = pyupbit.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    # 호가창을 조회해서 최우선 매도 호가를 조회
    unit = (krw*0.9995)/float(sell_price)
    # 원화 잔고를 최우선 매도가로 나눠서 구매 가능한 수량을 계산
    if krw > 5000:
        upbit.buy_market_order(ticker, unit)
    # 원화 5000원 이상일 때 매수하도록 설정

def sell_crypto_currency(ticker):
    unit = upbit.get_balance(ticker)[0]
    upbit.sell_market_order(ticker, unit)

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BORA")

# 로그인
access = "noaHpCDsB8CiRrL4z4kvrLzx9dcQUweqotnuCIBy"
secret = "vEZkSkdLbxJcWvql0jJOSfzJzJI6zIHjLNYI8A7W"

upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds = 10):
            target_price = get_target_price("BORA") 
            mid = datetime.datetime(now.year, now.month, now.second) + datetime.timedelta(1)
            sell_crypto_currency("BORA")
        # 프로그램에서 정확하게 1초 단위로 시각을 비교할 수 없음 
        # 따라서 특정 시각을 비교하는 것이 아니라 보다 긴 구간(10초)에 속하는 지를 확인하는 것 
        # 현재 시간(now)이 자정(mid)을 통과하는 순간 targe_price 갱신, mid 갱신, 코인 전량 매도      

        current_price = pyupbit.get_current_price("BORA")
        print(current_price)

        if current_price > target_price:
            buy_crypto_currency("BORA")
        time.sleep(1)
    
    except Exception as e:
        print(e)
        time.sleep(1)
           
        


    

