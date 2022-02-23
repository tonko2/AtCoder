from collections import deque

def euler_tour(G, root = 0):
    euler = []
    q = deque([root])
    q2 = deque()
    N = len(G)
    used = [False] * N
    while q:
        print(q, euler)
        u = q.pop()
        euler += [u]
        if used[u]:
            continue
        for v in G[u]:
            if used[v]:
                q += [v]
            else:
                q2 += [v]
        q.extend(q2)
        q2 = deque()
        used[u] = True
    return euler

# [L[v], R[v])
def euler(cu, pa = -1):
    global index
    L[cu] = index
    index += 1
    for to in G[cu]:
        if to != pa:
            euler(to, cu)
    R[cu] = index

L = [0] * 100010
R = [0] * 100010
N = 5
G = [[] for _ in range(N)]