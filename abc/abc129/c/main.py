import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
dp = [0] * (N + 1)
dp[0] = 1
d = defaultdict(int)
for i in range(M):
    a = ni()
    d[a] += 1

for i in range(N):
    if d[i + 1] == 0:
        dp[i + 1] += dp[i]
    if i + 2 <= N:
        if d[i + 2] == 0:
            dp[i + 2] += dp[i]
print(dp[N] % MOD)
