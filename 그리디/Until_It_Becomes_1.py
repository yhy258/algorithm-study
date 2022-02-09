"""
    어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
    1. 1을 빼기
    2. K로 나누기. (나누어 떨어질 때만 가능)
"""

def func(N, K):
    cnt = 0
    while N >= K :
        if N % K == 0 :
            N = N // K
        else :
            N -= 1
        cnt += 1

    while N > 1 :
        N -= 1
        cnt += 1

    return cnt

print(func(25, 5))