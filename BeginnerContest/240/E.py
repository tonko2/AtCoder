import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def leaf_order(u, p):
    global index
    if u != 0 and len(G[u]) == 1:
        leaf[u] = index + 1
        index += 1
        return
    for v in G[u]:
        if v != p:
            leaf_order(v, u)

def count_leaf(u, p):
    if leaf[u]:
        L[u] = R[u] = leaf[u]
        return
    for v in G[u]:
        if v == p:
            continue
        count_leaf(v, u)
        L[u] = min(L[u], L[v])
        R[u] = max(R[u], R[v])

N = ni()
L = [INF] * N
R = [-INF] * N
leaf = [0] * N
G = [[] for _ in range(N)]
index = 0

for i in range(N - 1):
    u, v = na()
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

leaf_order(0, -1)
count_leaf(0, -1)

for i in range(N):
    print(L[i], R[i])