# 내 코드
def BNP(money, prices):
    stocks = 0  # 보유 주식 수
    for price in prices:
        if money >= price:
            stocks += money // price  # 최대한 매수
            money -= (money // price) * price
    return money + stocks * prices[-1]  # 최종 자산 계산

def TIMING(money, prices):
    stocks = 0
    up, down = 0, 0  # 연속 상승/하락 횟수

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:  # 상승
            up += 1
            down = 0
        elif prices[i] < prices[i - 1]:  # 하락
            down += 1
            up = 0
        else:  # 가격 동일
            up, down = 0, 0

        if down >= 3 and money >= prices[i]:  # 3일 연속 하락 -> 매수
            stocks += money // prices[i]
            money -= (money // prices[i]) * prices[i]
        elif up >= 3 and stocks > 0:  # 3일 연속 상승 -> 매도
            money += stocks * prices[i]
            stocks = 0

    return money + stocks * prices[-1]  # 최종 자산 계산

# 입력 처리
money = int(input())
prices = list(map(int, input().split()))

bnp_result = BNP(money, prices)
timing_result = TIMING(money, prices)

# 결과 출력
if bnp_result > timing_result:
    print("BNP")
elif bnp_result < timing_result:
    print("TIMING")
else:
    print("SAMESAME")

##################################################
# 더 개선된 코드
def bnp_strategy(cash, prices):
    stocks = 0
    for price in prices:
        if cash >= price:
            stocks += cash // price
            cash %= price
    return cash + stocks * prices[-1]


def timing_strategy(cash, prices):
    stocks = 0
    for i in range(3, len(prices)):
        if prices[i - 3] < prices[i - 2] < prices[i - 1] < prices[i]:
            cash += stocks * prices[i]
            stocks = 0
        elif prices[i - 3] > prices[i - 2] > prices[i - 1] > prices[i]:
            stocks += cash // prices[i]
            cash %= prices[i]
    return cash + stocks * prices[-1]


def compare_strategies(cash, prices):
    bnp_result = bnp_strategy(cash, prices)
    timing_result = timing_strategy(cash, prices)

    if bnp_result > timing_result:
        return "BNP"
    elif bnp_result < timing_result:
        return "TIMING"
    else:
        return "SAMESAME"


# 입력 처리
cash = int(input().strip())
prices = list(map(int, input().split()))

# 결과 출력
print(compare_strategies(cash, prices))
