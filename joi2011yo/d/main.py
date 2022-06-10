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
A = na()
dp = [[0] * 21 for _ in range(N)]
dp[0][A[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if 0 <= j - A[i] <= 20:
            dp[i][j] += dp[i - 1][j - A[i]]
        if 0 <= j + A[i] <= 20:
            dp[i][j] += dp[i - 1][j + A[i]]

print(dp[N - 2][A[-1]])