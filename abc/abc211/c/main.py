import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
N = len(S)
dp = [[0] * 9 for _ in range(N + 1)]
for i in range(N):
    dp[i][0] = 1
str = "chokudai"
for i in range(N):
    for j in range(8):
        if S[i] == str[j]:
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
        else:
            dp[i + 1][j + 1] = dp[i][j + 1]

print(dp[N][8])