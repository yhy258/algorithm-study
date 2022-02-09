"""
    map이 주어진다. 1, 1 위치에서 n,m 위치 까지 가는데 최소 거리는 ? -> BFS로 가장 n, m에 먼저 도착하는 값을 저장해놓으면 된다.
    (시작점 1, 1은 무조건 값이 1이다.)
"""
from collections import deque
n, m = 5, 6
ground = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]


def find_path(x, y):
    queue = deque([(x,y)])
    visited = [(x, y)]
    while queue :

        nx, ny = queue.popleft()

        if nx - 1 >= 0 and (nx-1, ny) not in visited and ground[nx-1][ny]:
            queue.append((nx-1 ,ny))
            visited.append((nx-1, ny))
            ground[nx-1][ny] = ground[nx][ny] + 1

        if nx + 1 < n and (nx +1, ny) not in visited and ground[nx+1][ny]:
            queue.append((nx+1, ny))
            visited.append((nx+1, ny))
            ground[nx + 1][ny] = ground[nx][ny] + 1

        if ny -1 >= 0 and (nx, ny-1) not in visited and ground[nx][ny-1]:
            queue.append((nx, ny -1))
            visited.append((nx, ny-1))
            ground[nx][ny-1] = ground[nx][ny] + 1

        if ny +1 < m and (nx, ny + 1) not in visited and ground[nx][ny+1]:
            queue.append((nx, ny+1))
            visited.append((nx, ny+1))
            ground[nx][ny+1] = ground[nx][ny] + 1
    return ground[n-1][m-1]

visited = find_path(0 ,0)
print(visited)