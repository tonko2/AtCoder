import queue
import sys


sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, Q = na()
X = na()
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = na()
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

val = [[X[i]] for i in range(N)]

stack = [(0, -1, False)]
while stack:
    u, p, flag = stack.pop()
    if not flag:
        stack.append((u, p, True))
        for v in G[u]:
            if v != p:
                stack.append((v, u, False))
    else:
        for v in G[u]:
            if v == p:
                continue
            val[u] += val[v]
            val[u].sort(reverse=True)
            val[u] = val[u][:20]

for _ in range(Q):
    v, k = na()
    v -= 1
    k -= 1
    print(val[v][k])