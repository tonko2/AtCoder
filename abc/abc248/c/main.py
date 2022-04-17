import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 998244353

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M, K = na()
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(1, M + 1):
        for k in range(1, K + 1):
            if k - j >= 0:
                dp[i + 1][k] = (dp[i + 1][k] + dp[i][k - j]) % MOD

ans = 0
for i in range(K + 1):
    ans += dp[N][i]
print(ans % MOD)