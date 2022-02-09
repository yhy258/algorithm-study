from collections import deque

"""
    BFS : FIFO 타입의 Queue를 사용한다. 반복문으로 구현하기 편하다.
    DFS : Stack (Python의 list)를 사용한다. 재귀로 구현하기 알맞다. (깊게 들어가야하기 때문에.)
"""


def BFS(graph, root_node):
    visited = [root_node]
    queue = deque([root_node])

    while queue:
        now = queue.popleft()
        print(now)

        for k in sorted(graph[now]):
            if k not in visited:
                queue.append(k)
                visited.append(k)


# DFS 코드가 굉장히 간단하다. 하지만 재귀라 짜기 어려웠음.
def DFS(graph, now, visited):
    print(now)
    for k in sorted(list(graph[now])):
        if k not in visited :
            visited.append(k)
            DFS(graph, k, visited)








graph_list = {1: set([2, 3, 8]),
              2: set([1,7]),
              3: set([1,4,5]),
              4: set([3,5]),
              5: set([3,4]),
              6: set([7]),
              7: set([2,6,8]),
              8: set([1,7])}
root_node = 1
BFS(graph_list, root_node)
DFS(graph_list, root_node, [root_node])
