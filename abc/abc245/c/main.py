import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
B = na()
dp = [[False] * 2 for _ in range(N)]
dp[0][0] = True
dp[0][1] = True

for i in range(1, N):
    if abs(A[i - 1] - A[i]) <= K:
        dp[i][0] |= dp[i - 1][0]
    if abs(B[i - 1] - A[i]) <= K:
        dp[i][0] |= dp[i - 1][1]

    if abs(A[i - 1] - B[i]) <= K:
        dp[i][1] |= dp[i - 1][0]
    if abs(B[i - 1] - B[i]) <= K:
        dp[i][1] |= dp[i - 1][1]

if dp[N - 1][0] or dp[N - 1][1]:
    print("Yes")
else:
    print("No")