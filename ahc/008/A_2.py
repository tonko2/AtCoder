import queue
import sys
from collections import defaultdict
import random

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H = 31
W = 31

Flag = 1

dx = [1, 0, -1, 0, 0]
dy = [0, 1, 0, -1, 0]

basic_patterns = ['R', 'D', 'L', 'U', '.']
obstacle_pos = ['r', 'd', 'l', 'u']

# 0 -> 何もない
# 1 -> 人間
# 2 -> 動物
# 3 -> 障害物

animal_field = defaultdict(int)
obstacle_field = defaultdict(int)
human_field = defaultdict(int)
prev_human_field = defaultdict(int)

N = ni()
Px = [0] * N
Py = [0] * N
Pt = [0] * N
for i in range(N):
    Py[i], Px[i], Pt[i] = na()
    animal_field[(Px[i], Py[i])] += 1

M = ni()
Hx = [0] * M
Hy = [0] * M
Prev_hx = [0] * M
Prev_hy = [0] * M

for i in range(M):
    Hy[i], Hx[i] = na()
    human_field[(Hx[i], Hy[i])] += 1

move_patterns = [[None] * M for _ in range(300)]

def get_target_pos_right_up_corner():
    for i in range(1, W):
        for j in range(1, H):
            if i % 2 == 1:
                if j % 2 == 1:
                    if obstacle_field[(30 - i + 1, j + 1)] == 0:
                        return (30 - i + 1, j + 1)
            else:
                if j % 2 == 0:
                    if obstacle_field[(30 - i + 1, 30 - j + 1)] == 0:
                        return (30 - i + 1, 30 - j + 1)

def get_target_pos_left_up_corner():
    for i in range(1, W):
        for j in range(1, H):
            if i % 2 == 1:
                if j % 2 == 1:
                    if obstacle_field[(i, j + 1)] == 0:
                        return (i, j + 1)
            else:
                if j % 2 == 0:
                    if obstacle_field[(i, 30 - j + 1)] == 0:
                        return (i, 30 - j + 1)


def move_to_target_pos(x, y, target_pos):
    x2, y2 = target_pos

    if x <= x2:
        index = 0
    else:
        index = 2

    nx = x + dx[index]
    ny = y + dy[index]
    if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
        return (basic_patterns[index], nx, ny)

    if y <= y2:
        index = 1
    else:
        index = 3

    nx = x + dx[index]
    ny = y + dy[index]
    if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
        return (basic_patterns[index], nx, ny)

    return ('.', x, y)

'''
    q = queue.Queue()
    q.put((x, y, 0, 5))
    used = [[False] * W for _ in range(H)]
    while not q.empty():
        x, y, d, index = q.get()
        used[y][x] = True
        if x == x2 and y == y2:
            return (pos, x + dx[index], y + dy[index])
        if d > 6:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
                if d == 0:
                    index = i
                if used[ny][nx]:
                    continue
                q.put((nx, ny, d + 1, index))
'''


def is_adjacent(x, y, target_pos):
    x2, y2 = target_pos
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == x2 and ny == y2:
            return True
    return False

def can_move(x, y, target_pos):
    x2, y2 = target_pos
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == x2 and ny == y2:
            continue
        if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
            return True
    return False


def animal_movement(x, y, patterns):
    nx = x
    ny = y
    for pattern in patterns:
        index = basic_patterns.index(pattern)
        nx += dx[index]
        ny += dy[index]
    return (nx, ny)

def is_adjacent_animals(target_pos):
    x, y = target_pos
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and animal_field[(nx, ny)] > 0:
            return True
    return False

def is_put_obstacle(x, y, target_pos):
    x2, y2 = target_pos
    if obstacle_field[(x2, y2)] == 0 and human_field[(x2, y2)] == 0 and animal_field[(x2, y2)] == 0 and prev_human_field[(x2, y2)] == 0:
        return True
    else:
        return False

def put_obstacle(x, y, target_pos):
    x2, y2 = target_pos
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print(f'x = {x}, y = {y}, nx = {nx}, ny = {ny}, x2 = {x2}, y2 = {y2}')
        if nx == x2 and ny == y2:
            obstacle_field[(nx, ny)] += 1
            return obstacle_pos[i]

for turn in range(300):

    prev_human_field = human_field.copy()
    Prev_hx = Hx.copy()
    Prev_hy = Hy.copy()
    # 人間の行動
    for i in range(M):
        x, y = Hx[i], Hy[i]
        pos = "."
        human_field[(x, y)] -= 1

        if turn % 2 == 0:
            target_pos = get_target_pos_right_up_corner()
        else:
            target_pos = get_target_pos_right_up_corner()
            target_pos = get_target_pos_left_up_corner()

        if is_adjacent(x, y, target_pos):
            if not is_adjacent_animals(target_pos):
                if is_put_obstacle(x, y, target_pos):
                    pos = put_obstacle(x, y, target_pos)
        else:
            pos, x, y = move_to_target_pos(x, y, target_pos)

        Hx[i], Hy[i] = x, y
        human_field[(x, y)] += 1
        move_patterns[turn][i] = pos

    print("".join(move_patterns[turn]))

    # 動物の行動
    animal_movement_patterns = input().split()
    for i in range(N):
        x, y, t = Px[i], Py[i], Pt[i]
        animal_field[(x, y)] -= 1
        patterns = animal_movement_patterns[i]
        if t == 1: # 牛
            x, y = animal_movement(x, y, patterns)
        if t == 2: # 豚
            x, y = animal_movement(x, y, patterns)
        if t == 3: # うさぎ
            x, y = animal_movement(x, y, patterns)
        if t == 4: # 犬
            x, y = animal_movement(x, y, patterns)
        if t == 5: # 猫
            x, y = animal_movement(x, y, patterns)

        Px[i], Py[i] = x, y
        animal_field[(x, y)] += 1
