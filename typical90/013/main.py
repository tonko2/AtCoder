import sys
import math
import heapq
from collections import defaultdict, deque

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

N, M = na()
g = [[] for _ in range(N)]
for i in range(M):
    a, b, c = na()
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

ds = dijkstra(0)
de = dijkstra(N - 1)

for i in range(N):
    print(ds[i] + de[i])
