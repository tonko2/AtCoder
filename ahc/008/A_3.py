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
field = [[0] * W for _ in range(H)]

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

S = set()
all_tasks = [[] for _ in range(M)]

def set_circle_point(index, x, y, n):
    S = set()
    y_min = y - n
    y_max = y + n + 1
    x_min = x - n
    x_max = x + n + 1
    for i in range(y_min, y_max):
        for j in range(x_min, x_max):
            if i == y_min:
                if j >= 1 and j < W and i >= 1 and i < H:
                    if j == x_min:
                        continue
                    if j == x_max - 1:
                        continue
                    # (y, -x)
                    S.add((i, -j))
            if i == y_max - 1:
                if j >= 1 and j < W and i >= 1 and i < H:
                    if j == x_min:
                        continue
                    if j == x_max - 1:
                        continue
                    S.add((i, -j))
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            if i == x_min:
                if j >= 1 and j < H and i >= 1 and i < W:
                    if j == y_min:
                        continue
                    if j == y_max - 1:
                        continue
                    S.add((j, -i))
            if i == x_max - 1:
                if j >= 1 and j < H and i >= 1 and i < W:
                    if j == y_min:
                        continue
                    if j == y_max - 1:
                        continue
                    S.add((j, -i))

        all_tasks[index] = sorted(list(S))

def is_near(x, y, x2, y2):
    return abs(x - x2) + abs(y - y2) <= 6

for i in range(M):
    x, y = Hx[i], Hy[i]
    set_circle_point(i, x, y, 5)

for i in range(M):
    for j in range(len(all_tasks[i])):
        y, x = all_tasks[i][j]
        all_tasks[i][j] = (-x, y)

for i in range(M):
    x, y = Hx[i], Hy[i]
    for j in range(i + 1, M):
        x2, y2 = Hx[j], Hy[j]
        if is_near(x, y, x2, y2):
            all_tasks[i] = all_tasks[j]

move_patterns = [[None] * M for _ in range(300)]



def animal_movement(x, y, patterns):
    nx = x
    ny = y
    for pattern in patterns:
        index = basic_patterns.index(pattern)
        nx += dx[index]
        ny += dy[index]
    return (nx, ny)

def is_adjacent(x, y, target_pos):
    x2, y2 = target_pos
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == x2 and ny == y2:
            return True
    return False

def is_adjacent_animals(target_pos):
    x, y = target_pos
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and animal_field[(nx, ny)] > 0:
            return True
    return False

def is_put_obstacle(target_pos):
    x, y = target_pos
    if obstacle_field[(x, y)] == 0 and human_field[(x, y)] == 0 and animal_field[(x, y)] == 0 and prev_human_field[(x, y)] == 0:
        return True
    else:
        return False

def put_obstacle(x, y, target_pos):
    x2, y2 = target_pos
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == x2 and ny == y2:
            obstacle_field[(nx, ny)] += 1
            return obstacle_pos[i]

def move_to_target_pos(x, y, target_pos):
    x2, y2 = target_pos

    random_order = random.randint(0, 1)
    if random_order:
        index = -1
        if x < x2:
            index = 0
        if x > x2:
            index = 2

        if index != -1:
            nx = x + dx[index]
            ny = y + dy[index]
            if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
                return (basic_patterns[index], nx, ny)

        index = -1
        if y < y2:
            index = 1
        if y > y2:
            index = 3

        if index != -1:
            nx = x + dx[index]
            ny = y + dy[index]
            if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
                return (basic_patterns[index], nx, ny)
    else:
        if random_order:
            index = -1
            if y < y2:
                index = 1
            if y > y2:
                index = 3

            if index != -1:
                nx = x + dx[index]
                ny = y + dy[index]
                if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
                    return (basic_patterns[index], nx, ny)

            index = -1
            if x < x2:
                index = 0
            if x > x2:
                index = 2

            if index != -1:
                nx = x + dx[index]
                ny = y + dy[index]
                if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
                    return (basic_patterns[index], nx, ny)

    if x == x2:
        random_index = random.randint(0, 1)
        index = [0, 2][random_index]
        nx = x + dx[index]
        ny = y + dy[index]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
            return (basic_patterns[index], nx, ny)

    if y == y2:
        random_index = random.randint(0, 1)
        index = [1, 3][random_index]
        nx = x + dx[index]
        ny = y + dy[index]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
            return (basic_patterns[index], nx, ny)

    return ('.', x, y)

def most_nearest_pos(x, y, tasks):
    dis = float('inf')
    res = (x, y)
    for i in range(len(tasks)):
        x2, y2 = tasks[i]
        d = abs(x - x2) + abs(y - y2)
        if dis > d:
            dis = d
            res = (x2, y2)
    return res

def move_random(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < W and ny < H and nx >= 1 and ny >= 1 and obstacle_field[(nx, ny)] == 0:
            return (basic_patterns[i], nx, ny)
    return (".", x, y)

for turn in range(300):

    prev_human_field = human_field.copy()

    if 70 <= turn <= 75 or 100 <= turn <= 105 or 160 <= turn <= 170 or 220 <= turn <= 225 or 270 <= turn <= 275:
        for i in range(M):
            x, y = Hx[i], Hy[i]
            human_field[(x, y)] -= 1
            pos, x, y = move_random(x, y)
            Hx[i], Hy[i] = x, y
            human_field[(x, y)] += 1
            move_patterns[turn][i] = pos

    # 人間の行動
    else:
        for i in range(M):
            x, y = Hx[i], Hy[i]
            human_field[(x, y)] -= 1
            tasks = all_tasks[i]
            if len(tasks) == 0:
                pos = '.'
            else:
                flag = False
                for j in range(len(tasks)):
                    target_pos = tasks[j]
                    if is_adjacent(Hx[i], Hy[i], target_pos) and not is_adjacent_animals(target_pos) and is_put_obstacle(target_pos):
                        flag = True
                        pos = put_obstacle(Hx[i], Hy[i], target_pos)
                        field[target_pos[1]][target_pos[0]] = 1
                        x, y = Hx[i], Hy[i]
                        tasks.pop(j)
                        break
                if not flag:

                    random_task = random.randint(0, len(tasks) - 1)
                    if turn <= 120:
                        target_pos = tasks[0]
                    elif turn <= 150:
                        target_pos = tasks[len(tasks) - 1]
                    #    target_pos = most_nearest_pos(Hx[i], Hy[i], tasks)
                    else:
                        target_pos = tasks[random_task]
                    # 障害物置くか移動
                    if is_adjacent(Hx[i], Hy[i], target_pos) and not is_adjacent_animals(target_pos) and is_put_obstacle(target_pos):
                        pos = put_obstacle(Hx[i], Hy[i], target_pos)
                        field[target_pos[1]][target_pos[0]] = 1
                        x, y = Hx[i], Hy[i]
                    else:
                        pos, x, y = move_to_target_pos(Hx[i], Hy[i], target_pos)

            human_field[(x, y)] += 1
            move_patterns[turn][i] = pos
            Hx[i], Hy[i] = x, y

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
