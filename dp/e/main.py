import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, W = na()
w = [0] * N
v = [0] * N

for i in range(N):
    w[i], v[i] = na()

V = 100000
dp = [[INF] * (V + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(V + 1):
        if j - v[i] >= 0:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
        else:
            dp[i + 1][j] = dp[i][j]

ans = 0
for i in range(V + 1):
    if dp[N][i] <= W:
        ans = max(ans, i)
print(ans)

