import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, depth):
    global ans
    ans = max(ans, depth)
    grid[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < W and ny < H and nx >= 0 and ny >= 0 and grid[ny][nx]:
            dfs(nx, ny, depth + 1)
    grid[y][x] = 1
W = ni()
H = ni()
grid = []
for _ in range(H):
    grid.append(na())

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 1:
            dfs(j, i, 1)
print(ans)