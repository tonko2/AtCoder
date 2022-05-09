import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(pos, pre):
    dp[pos] = 1
    for v in G[pos]:
        if v == pre:
            continue
        dfs(v, pos)
        dp[pos] += dp[v]

N = ni()
A = [0] * (N - 1)
B = [0] * (N - 1)
dp = [0] * (N)
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = na()
    a -= 1
    b -= 1
    A[i] = a
    B[i] = b
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

dfs(0, -1)
ans = 0
for i in range(N - 1):
    r = min(dp[A[i]], dp[B[i]])
    ans += r * (N - r)
print(ans)
