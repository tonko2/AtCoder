import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W = na()
tmp_grid = []
for _ in range(H):
    tmp_grid.append(ns())

grid = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if tmp_grid[i][j] != '.':
            grid[i][j] = int(tmp_grid[i][j])

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

ans = []
for i in range(H):
    for j in range(W):
        if grid[i][j] != 0:
            continue
        nums = [1, 2, 3, 4, 5]
        for k in range(4):
            nx = j + dx[k]
            ny = i + dy[k]
            if nx >= 0 and ny >= 0 and nx < W and ny < H and grid[ny][nx] != 0:
                if nums.count(grid[ny][nx]):
                    nums.remove(grid[ny][nx])
        grid[i][j] = nums[0]

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(str(grid[i][j]))
    print("".join(ans))