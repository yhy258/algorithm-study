def move_knight(now):
    alphabet_int = ord('a')-1

    i, j = int(now[1]), ord(now[0]) - alphabet_int

    move_type = [(1, 2), (-1, 2),(1, -2), (-1, -2), (2, 1),(2, -1), (-2, 1), (-2, -1)]
    cnt = 0
    for move in move_type:
        di, dj = move
        if (i + di) < 1 or (j + dj) < 1 or (i + di) > 8 or (j + dj) >8 :
            continue
        cnt += 1

    return cnt

print(move_knight('a1'))