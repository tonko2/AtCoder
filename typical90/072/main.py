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
used = [[False] * 20 for _ in range(20)]

def dfs(sx, sy, x, y):
    if sx == x and sy == y and used[y][x]:
        return 0

    used[y][x] = True

    res = -1000
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or ny >= H or nx >= W or grid[ny][nx] == '#':
            continue
        if (sx != nx or sy != ny) and used[ny][nx]:
            continue
        res = max(res, dfs(sx, sy, nx, ny) + 1)

    used[y][x] = False
    return res
H, W = na()
grid = []
for _ in range(H):
    grid.append(ns())

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            continue
        ans = max(ans, dfs(j, i, j, i))

if ans <= 2:
    print(-1)
else:
    print(ans)