import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(r, total, p):
    total += counter[r]
    ans[r] = total
    for v in G[r]:
        if p == v:
            continue
        dfs(v, total, r)

N, Q = na()
counter = [0] * N
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = na()
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
for _ in range(Q):
    p, x = na()
    p -= 1
    counter[p] += x
ans = [0] * N
dfs(0, 0, -1)
print(*ans)