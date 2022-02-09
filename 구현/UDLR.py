"""
    상하좌우 문제. (1, 1)에서 시작한다.
    R R R U D D -> 3,4
"""

def UDLR(map_size : int, control_list : list) -> tuple :
    i, j = 1, 1 # row, col
    for control in control_list :
        # 예외 처리.
        if (i == 1 and control == "U") or (i == map_size and control == "D") or (j == 1 and control == "L") or (j == map_size and control == "R") :
            continue
        if control == "U":
            i -= 1
        elif control == "D":
            i += 1
        elif control == "L" :
            j -= 1
        else :
            j += 1
    return (i, j)

map_size = 5
control_list = "R R R U D D".split(" ")
print(UDLR(map_size, control_list))