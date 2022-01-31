import sys
import heapq

sys.setrecursionlimit(10**6)
stdin = sys.stdin

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

if __name__ == "__main__":
    na = lambda: list(map(int, stdin.readline().split()))

    N, M = na()
    H = na()
    g = [[] for _ in range(N)]
    for i in range(M):
        u, v, cost = na()
        u, v = u - 1, v - 1
        g[u].append((v, cost))
        g[v].append((u, cost))
    dijkstra(0)