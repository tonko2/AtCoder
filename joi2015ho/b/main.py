import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def rec(i, j):
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if (N - (j - i + 1)) % 2 == 0:
        dp[i][j] = max(rec(i + 1, j) + A[i], rec(i, j - 1) + A[j])
        return dp[i][j]
    else:
        if A[i] > A[j]:
            dp[i][j] = rec(i + 1, j)
            return dp[i][j]
        else:
            dp[i][j] = rec(i, j - 1)
            return dp[i][j]

N = ni()
A = []
for _ in range(N):
    A.append(ni())
A += A
dp = [[-1] * (2 * N + 1) for _ in range(2 * N + 1)]
ans = 0
for i in range(N):
    ans = max(ans, rec(i, i + N - 1))
print(ans)