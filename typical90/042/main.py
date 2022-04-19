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

K = ni()
if K % 9 != 0:
    print(0)
else:
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(1, K + 1):
        j = min(i, 9)
        for j in range(1, j + 1):
            dp[i] = (dp[i] + dp[i - j]) % MOD
    print(dp[K])