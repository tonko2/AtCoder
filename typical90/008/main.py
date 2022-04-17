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

N = ni()
S = ns()

dp = [[0] * 8 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(8):
        dp[i + 1][j] += dp[i][j]
        if S[i] == 'a' and j == 0:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == 't' and j == 1:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == 'c' and j == 2:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == 'o' and j == 3:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == 'd' and j == 4:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == 'e' and j == 5:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == 'r' and j == 6:
            dp[i + 1][j + 1] += dp[i][j]
    for j in range(8):
        dp[i + 1][j] %= MOD
print(dp[N][7])