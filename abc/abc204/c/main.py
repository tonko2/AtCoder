import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(s, e):
    if used[s][e]:
        return
    used[s][e] = True
    for nxt in g[e]:
        if not used[s][nxt]:
            dfs(s, nxt)

N, M = na()
used = [[False] * N for _ in range(N)]

g = [[] for _ in range(N)]
for i in range(M):
    a, b = na()
    a -= 1
    b -= 1
    g[a].append(b)

for i in range(N):
    dfs(i, i)

ans = 0
for i in range(N):
    for j in range(N):
        if used[i][j]:
            ans += 1
print(ans)