import sys
import math
from collections import defaultdict, deque
import heapq

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dijkstra(start):
    ds = [float('inf')] * N
    h = []
    ds[start] = 0
    heapq.heappush(h, (0, start))
    while len(h) > 0:
        min_cost, u = heapq.heappop(h)
        if min_cost > ds[u]:
            continue

        for v, d in g[u]:
            if ds[u] + d < ds[v]:
                ds[v] = ds[u] + d
                heapq.heappush(h, (ds[v], v))
    return ds

N = ni()
g = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = na()
    g[a - 1].append((b - 1, 1))
    g[b - 1].append((a - 1, 1))
ds = dijkstra(0)
tree_len = 0
v = 0
for i in range(N):
    if ds[i] != INF and tree_len < ds[i]:
        tree_len = ds[i]
        v = i
ds = dijkstra(v)
ans = 0
for i in range(N):
    if ds[i] != INF:
        ans = max(ans, ds[i])
print(ans + 1)