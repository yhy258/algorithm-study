"""
    다양한 수로 이루어진 배열이 주어졌을 때 M번 더하여 가장 큰 수를 만들자. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 이상 나오면 안된다.

"""

def bignumber_iter(arr, N, M, K):

    arr = sorted(arr)
    largest, second = arr[-1], arr[-2]

    all = (largest * K + second) * (M // (K + 1)) + M % (K + 1) * largest

    return all

N = 5
M = 8
K = 3
arr = [2,4,5,4,6]
print(bignumber_iter(arr, N, M, K))