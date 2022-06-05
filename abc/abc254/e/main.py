import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(v, k, cnt, S):
    S.add(v)
    if cnt == k:
        return
    for to in G[v]:
        dfs(to, k, cnt + 1, S)

N, M = na()
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = na()
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
Q = ni()
for _ in range(Q):
    x, k = na()
    S = set()
    dfs(x - 1, k, 0, S)
    ans = 0
    for s in S:
        ans += s + 1
    print(ans)