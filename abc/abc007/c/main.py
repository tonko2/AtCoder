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

def bfs():
    q = deque()
    q.append((sx, sy, 0))
    while q:
        x, y, cnt = q.popleft()
        if x == gx and y == gy:
            return used[gy][gx]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < C and ny < R and nx >= 0 and ny >= 0 and grid[ny][nx] == '.' and used[ny][nx] == INF:
                used[ny][nx] = cnt + 1
                q.append((nx, ny, cnt + 1))
    return -1
R, C = na()
sy, sx = na()
gy, gx = na()
grid = []
for _ in range(R):
    grid.append(ns())

sy -= 1
sx -= 1
gy -= 1
gx -= 1
used = [[INF] * C for _ in range(R)]

print(bfs())
