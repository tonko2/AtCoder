import heapq

def prim(G, N):
    used = [0] * N
    que = [(c, v) for v, c in G[0]]
    used[0] = 1
    heapq.heapify(que)

    res = 0
    while que:
        c, u = heapq.heappop(que)
        if used[u]:
            continue
        used[u] = 1
        res += c
        for v, c in G[u]:
            if used[v]:
                continue
            heapq.heappush(que, (c, v))
    return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        # u: 始点
        # v: 終点
        # c: コスト
        u, v, c = map(int ,input().split())
        u -= 1
        v -= 1
        G[u].append((v, c))
    cost = prim(G, N)
    print(cost)