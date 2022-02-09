import sys

"""
    여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.
    하지만 룰을 지켜야한다.
    1. 숫자가 N x M 형태로 놓여진다. (행렬)
    2. 먼저 뽑고자 하는 행을 선택
    3. 해당 행의 가장 낮은 숫자를 뽑는다.
     -> 이런 룰을 통해 가장 큰 수를 뽑아야한다. 행을 잘 골라야한다.
"""


def number_card_game(N, M, card_matrix):
    maximal = - sys.maxsize
    for row in card_matrix:
        if maximal < min(row):
            maximal = min(row)
    return maximal



N, M = 2, 4
card_matrix = [[7,3,1,8], [3,3,3,4]]
print(number_card_game(N, M, card_matrix))
