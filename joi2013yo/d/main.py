import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

D, N = na()
T = []
for _ in range(D):
    T.append(ni())
min_t = []
max_t = []
C = []
for _ in range(N):
    a, b, c = na()
    min_t.append(a)
    max_t.append(b)
    C.append(c)
# dp[Days][選んだ服]
dp = [[0] * N for _ in range(D + 1)]

for i in range(1, D):
    for j in range(N):
        for k in range(N):
            if min_t[k] <= T[i] <= max_t[k] and min_t[j] <= T[i - 1] <= max_t[j]:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + abs(C[k] - C[j]))
            else:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j])

ans = 0
for i in range(N):
    ans = max(ans, dp[D][i])
print(ans)