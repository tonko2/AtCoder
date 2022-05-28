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
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(M + 1):
    dp[1][i] = 1

for i in range(1, N):
    A = [0, dp[i][1]]
    for j in range(2, M + 1):
        A.append((A[j - 1] + dp[i][j]))
    for j in range(1, M + 1):
        flag1 = False
        flag2 = False
        if j + K <= M:
            dp[i + 1][j] = (dp[i + 1][j] + A[M] - (A[j + K - 1])) % MOD
            flag1 = True
        if j - K >= 1:
            dp[i + 1][j] = (dp[i + 1][j] + A[j - K]) % MOD
            flag2 = True
        if flag1 and flag2 and K == 0:
            dp[i + 1][j] -= A[j] - A[j - 1]

ans = 0
for i in range(1, M + 1):
    ans = (ans + dp[N][i]) % MOD
print(ans)
