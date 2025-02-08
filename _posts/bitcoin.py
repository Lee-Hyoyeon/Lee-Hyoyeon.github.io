import requests
import time
import requests

API_KEY = "355ab7a9de72eb044ca57ff8cdf464a8799a9846eaf6c2"
API_SECRET = "MGNmNWIyM2Y0ZDQ5MjcyMmJkYTNkZTczZTcwNzNhZDU3OWZjYzZmYjYxYTI3ODlhOTY0N2VhZjRjMGNkNg=="


def get_balance():
    """ 빗썸 잔액 조회 함수 """
    endpoint = "/info/balance"
    params = {"currency": "BTC"}

    response = requests.post(f"{API_URL}{endpoint}", headers=get_headers(endpoint, params), data=params)
    return response.json()


# 실행
balance = get_balance()
print(balance)  # 현재 원화(KRW)와 보유 코인(BTC) 잔액 출력
def get_current_price():
    """ 현재 BTC 시세 가져오기 """
    response = requests.get("https://api.bithumb.com/public/ticker/BTC_KRW")
    data = response.json()
    return float(data["data"]["closing_price"])

def buy_btc(price, quantity):
    """ 지정가 매수 주문 """
    print(f"💰 {price} KRW에 {quantity} BTC 매수 주문 실행!")
    # 실제 API 매수 요청 코드가 들어가야 함

def sell_btc(price, quantity):
    """ 지정가 매도 주문 """
    print(f"📈 {price} KRW에 {quantity} BTC 매도 주문 실행!")
    # 실제 API 매도 요청 코드가 들어가야 함

# 매매 전략
BUY_PRICE = 49500000  # 4950만원 이하일 때 매수
SELL_PERCENT = 1.05  # 5% 이상 오르면 매도
BTC_AMOUNT = 0.01  # 0.01 BTC 거래

bought_price = None  # 매수 가격 저장

while True:
    current_price = get_current_price()
    print(f"현재 BTC 가격: {current_price} KRW")

    if bought_price is None and current_price <= BUY_PRICE:
        buy_btc(current_price, BTC_AMOUNT)
        bought_price = current_price  # 매수 가격 저장

    if bought_price and current_price >= bought_price * SELL_PERCENT:
        sell_btc(current_price, BTC_AMOUNT)
        bought_price = None  # 다시 매수 대기

    time.sleep(10)  # 10초마다 시세 확인


