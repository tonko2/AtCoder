import sys
import random
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H = 31
W = 31
# 0 -> 何もない
# 1 -> 人間
# 2 -> 動物
# 3 -> 障害物
field = [[0] * W for _ in range(H)]
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
for i in range(M):
    Hy[i], Hx[i] = na()
    human_field[(Hx[i], Hy[i])] += 1


move_patterns = [[None] * M for _ in range(300)]

def most_nearest_pos(x, y):
    dis = float('inf')
    res = (x, y)
    for i in range(N):
        x2, y2 = Px[i], Py[i]
        if x == x2 and y == y2:
            continue
        d = abs(x - x2) + abs(y - y2)
        if dis > d:
            dis = d
            res = (x2, y2)
    return res

def count_obstacles(x, y):
    return obstacle_field[(x + 1, y)] + obstacle_field[(x - 1, y)] + obstacle_field[(x, y + 1)] + obstacle_field[(x, y - 1)]

def animal_movement(x, y, patterns):
    basic_patterns = ['R', 'D', 'L', 'U', '.']
    dx = [1, 0, -1, 0, 0]
    dy = [0, 1, 0, -1, 0]
    nx = x
    ny = y
    for pattern in patterns:
        index = basic_patterns.index(pattern)
        nx += dx[index]
        ny += dy[index]
    return (nx, ny)

def canMove(x, y):
    return True

def search_human(x, y):
    for i in range(1, H):
        for j in range(1, W):
            if j == x and i == y:
                continue
            if human_field[(j, i)] > 0:
                return (j, i)

def is_adjacent_animals(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and animal_field[(nx, ny)] > 0:
            return True
    return False

def put_obstacle(x, y, near_pos):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    pos = ['r', 'd', 'l', 'u']

    # 一番近い動物側に障害物を置く
    x2, y2 = near_pos
    if abs(x - x2) <= abs(y - y2):
        if x <= x2:
            index = 0 # r
        else:
            index = 2 # l
    else:
        if y <= y2:
            index = 1 # d
        else:
            index = 3 # u
    nx = x + dx[index]
    ny = y + dy[index]
    if nx < W and ny < H and nx >= 1 and ny >= 1 and prev_human_field[(nx, ny)] == 0 and human_field[(nx, ny)] == 0 and animal_field[(nx, ny)] == 0 and obstacle_field[(nx, ny)] == 0 and not is_adjacent_animals(nx, ny):
        return (pos[index], nx, ny)

    # 置けない場合はランダム
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and prev_human_field[(nx, ny)] == 0 and human_field[(nx, ny)] == 0 and animal_field[(nx, ny)] == 0 and obstacle_field[(nx, ny)] == 0 and not is_adjacent_animals(nx, ny):
            return (pos[i], nx, ny)

    # どこも置けない時はその場に留まる
    return ('.', x, y)

def move(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    pos = ['R', 'D', 'L', 'U']
    cnt = 0
    while True:
        if cnt > 50:
            break
        pattern = random.randint(0, 3)
        nx = x + dx[pattern]
        ny = y + dy[pattern]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
            return (pos[pattern], nx, ny)
        cnt += 1
    return ('.', x, y)

for turn in range(300):
    # 人間の行動
    prev_human_field = human_field.copy()
    for i in range(M):
        x, y = Hx[i], Hy[i]

        near_animal_pos = most_nearest_pos(x, y)

        # 障害物 -> 動く -> 止まるの優先順位
        pos = '.'
        if turn >= 100:
            (pos, x, y) = put_obstacle(x, y, near_animal_pos)
        if pos == '.':
            human_field[(x, y)] -= 1
            (pos, x, y) = move(x, y)
            Hx[i], Hy[i] = x, y
            human_field[(x, y)] += 1
        else:
            obstacle_field[(x, y)] += 1
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
