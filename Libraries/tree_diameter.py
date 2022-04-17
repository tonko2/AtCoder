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

def tree_diameter():
    ds = dijkstra(0)
    tree_len = 0
    v = 0
    for i in range(N):
        if ds[i] != INF and tree_len < ds[i]:
            tree_len = ds[i]
            v = i
    ds = dijkstra(v)
    res = 0
    for i in range(N):
        if ds[i] != INF:
            res = max(res, ds[i])
            
N = 10