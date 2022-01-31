import sys
import heapq

sys.setrecursionlimit(10 ** 6)

def solve():
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

    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    g = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        if H[u] > H[v]:
            u, v = v, u
        g[u].append((v, H[v] - H[u]))
        g[v].append((u, 0))

    ds = dijkstra(0)
    ans = 0
    for i in range(N):
        ans = max(ans, (H[0] - H[i]) - ds[i])
    print(ans)

if __name__ == "__main__":
    solve()
