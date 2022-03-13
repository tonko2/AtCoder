import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, L = na()
dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
    if i + L <= N:
        dp[i + L] = (dp[i + L] + dp[i]) % MOD

print(dp[N])