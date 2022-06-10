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

def bfs(sx, sy, gx, gy):
    q = deque()
    q.append((sx, sy, 0))
    while q:
        x, y, cnt = q.popleft()
        if x == gx and y == gy:
            return used[y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < W and ny < H and used[ny][nx] == INF and grid[ny][nx] != 'X':
                used[ny][nx] = cnt + 1
                q.append((nx, ny, cnt + 1))
    return -1
H, W, N = na()
grid = []
for _ in range(H):
    grid.append(ns())
candidates = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            candidates.append((i, j))

for k in range(N):
    for i in range(H):
        for j in range(W):
            if chr(ord('1') + k) == grid[i][j]:
                candidates.append((i, j))

ans = 0
used = [[INF] * W for _ in range(H)]
for i in range(len(candidates) - 1):
    sy, sx = candidates[i]
    gy, gx = candidates[i + 1]
    used = [[INF] * W for _ in range(H)]
    used[sy][sx] = 0
    ans += bfs(sx, sy, gx, gy)
print(ans)
