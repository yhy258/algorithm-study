"""
    게임 개발.
    N x M map

    map 주어짐. 0 : 육지 1 : 바다

    방향 : 0 : 북, 1 : 동, 2: 남, 3 : 서

    4 4 : 4 x 4 맵 생성
    1 1 0 : 1 1 위치에서 0 방향 (북)
    1 1 1 1
    1 0 0 1
    1 1 0 1
    1 1 1 1  맵.

    1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향을 회전한 뒤 갈 곳을 정한다.
     _ 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 해당 칸으로 한칸 전진. 가보지 않은 칸이 없다면 왼쪽방향으로 회전만 수행한다. 다시 1.
    2. 만약 네 방향 모두 이미 가본칸이거나 바다로 되어 있으면 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 갈 수 없으면 end.

    방문 : -1 로 특정하자.
"""
def minus_dir(dir):
    if dir == 0 :
        return 3
    else :
        return dir - 1

def move_game(map_size, coord_direction, map_):

    move_type = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    N, M = map_size
    i, j = coord_direction[0:2]
    direction = coord_direction[2]
    dir_limit = 0
    meet_cnt = 0
    while True:
        direction = minus_dir(direction)
        if i + move_type[direction][0] < 0 or j + move_type[direction][1] < 0 or i + move_type[direction][0] > N - 1 or j + move_type[direction][1] > M - 1 or map_[i + move_type[direction][0]][j + move_type[direction][1]] != 0:
            dir_limit += 1
        else :
            i, j = i + move_type[direction][0], j + move_type[direction][1]
            map_[i][j] = -1
            dir_limit = 0
            meet_cnt +=1

        if dir_limit == 4:
            if i - move_type[direction][0] < 0 or j - move_type[direction][1] < 0 or i - move_type[direction][0] > N -1 or j - move_type[direction][1] > M - 1 or map_[i - move_type[direction][0]][j - move_type[direction][1]] == 1:
                break
            else :
                i, j = i - move_type[direction][0],  j - move_type[direction][1]
                dir_limit = 0
    return meet_cnt

map_size = (4, 4)
coord_direction = (1, 1, 0)
map_ = [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]
print(move_game(map_size, coord_direction, map_))