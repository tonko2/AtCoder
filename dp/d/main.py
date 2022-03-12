import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, W = na()
dp = [[0] * (W + 1) for _ in range(N + 1)]
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = na()

for i in range(N):
    for j in range(W + 1):
        if j - w[i] >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][W])