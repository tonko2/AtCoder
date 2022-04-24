import heapq
import queue
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    field = [INF] * (H * W * 4)
    for i in range(4):
        field[(sy * W + sx) * 4 + i] = 0
    q = deque()
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if nx >= 0 and ny >= 0 and nx < W and ny < H and grid[ny][nx] == '.':
            q.append((nx, ny, i, 0))
            field[(ny * W + nx) * 4 + i] = 0
    while q:
        x, y, d, cnt = q.popleft()
        if cnt > field[(y * W + x) * 4 + d]:
            continue
        if x == gx and y == gy:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < W and ny < H and grid[ny][nx] == '.':
                nv = (ny * W + nx) * 4 + i
                if i == d:
                    if cnt >= field[nv]:
                        continue
                    field[nv] = cnt
                    q.appendleft((nx, ny, i, cnt))
                else:
                    if cnt + 1 >= field[nv]:
                        continue
                    field[nv] = cnt + 1
                    q.append((nx, ny, i, cnt + 1))

    return -1

H, W = na()
sy, sx = na()
gy, gx = na()
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
grid = []
for i in range(H):
    grid.append(ns())
print(bfs())