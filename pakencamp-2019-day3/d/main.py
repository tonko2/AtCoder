import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
grid = []
for _ in range(5):
    grid.append(ns())
# dp[列][色]
dp = [[INF] * 3 for _ in range(N + 1)]
for i in range(3):
    dp[0][i] = 0
cnt = [[0] * 3 for _ in range(N)]
for i in range(N):
    for j in range(3):
        r = 0
        b = 0
        w = 0
        for k in range(5):
            if grid[k][i] == 'R':
                r += 1
            if grid[k][i] == 'B':
                b += 1
            if grid[k][i] == 'W':
                w += 1
        cnt[i][0] = r
        cnt[i][1] = b
        cnt[i][2] = w
for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + 5 - cnt[i][k])
ans = INF
for i in range(3):
    ans = min(ans, dp[N][i])
print(ans)