"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

# 1. Greedy 한 성격을 띄는가? 10 -> 10 - 1 / 3 (dp로 풀자.)
# Bottom up; 경우를 모두 고려.
"""
    N = 1 -> 0
    N = 2 -> 1
    N = 3 -> 1
    N = 4 -> 2
    N = 5 -> 3
    ...
    
    d[N] = d[N-1] + 1
    if N % 3 == 0 :
        min(d[N//3] + 1, d[N]) # 나눴을 때랑 그냥 뺐을때 뭐가 더 작은가?
    if N % 2 == 0 :
    ... 이런식으로
"""

N = int(input())

memory = [0] * (N+1)
memory[1] = 0

def f(N):
    for i in range(2, N+1):
        memory[i] = memory[i-1] + 1
        if i % 3 == 0 :
            memory[i] = min(memory[i], memory[i//3] + 1)

        if i % 2 == 0 :
            memory[i] = min(memory[i], memory[i//2] + 1)

f(N)
print(memory[N])


