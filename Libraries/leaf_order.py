import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

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

'''
3
2 1
3 1 
'''
index = 0
N = ni()
leaf = [-float('inf')] * N
L = [0] * N
R = [0]* N
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = na()
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

leaf_order(0, -1)
print(leaf)


