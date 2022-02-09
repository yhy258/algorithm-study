"""
    카운터에는 거스름돈으로 사용할 500원, 100원 50원, 10원짜리 동전이 무한히 존재한다.
    손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수.
"""

def COINCHANGER(N):
    coin_n = 0
    for i in [500, 100, 50, 10]:

        if N >= i :
            coin_n += N//i
            N = N % i

    return coin_n

print(COINCHANGER(1260))


