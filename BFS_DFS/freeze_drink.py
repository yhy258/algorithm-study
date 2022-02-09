"""
    얼음 틀이 있다. 0의 경우 액체를 넣을 수 있는, 1의 경우 가림막.
    얼음 틀을 사용했을 때 몇개의 조각을 얻을 수 있는가?
"""

freeze_map = [[0,0,1,1,0],
              [0,0,0,1,1],
              [1,1,1,1,1],
              [0,0,0,0,0]]


def dfs(i, j, n, m):

    if i < 0 or i >= n or j < 0 or j >= m :
        return False

    if freeze_map[i][j] == 0 :
        freeze_map[i][j] = 1
        dfs(i - 1, j, n, m)
        dfs(i + 1, j, n, m)
        dfs(i, j - 1, n, m)
        dfs(i, j + 1, n, m)
        return True
    return False

result = 0
for i in range(4):
    for j in range(5):
        if dfs(i,j,4,5) == True:
            result += 1

print(result)




