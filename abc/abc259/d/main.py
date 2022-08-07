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

def is_cross(x, y, r, x2, y2, r2):
    d = (x - x2) ** 2 + (y - y2) ** 2
    return d == (r - r2) ** 2 or (r - r2) ** 2 < d < (r + r2) ** 2 or d == (r + r2) ** 2

def dfs(v):
    if v == end:
        print("Yes")
        exit()
    used[v] = True
    for to in G[v]:
        if used[to]:
            continue
        dfs(to)

N = ni()
Sx, Sy, Tx, Ty = na()
X = []
Y = []
R = []
start = -1
end = -1
for i in range(N):
    x, y, r = na()
    X.append(x)
    Y.append(y)
    R.append(r)
    if r * r == (x - Sx) ** 2 + (y - Sy) ** 2:
        start = i
    if r * r == (x - Tx) ** 2 + (y - Ty) ** 2:
        end = i

G = [[] for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if is_cross(X[i], Y[i], R[i], X[j], Y[j], R[j]):
            G[i].append(j)
            G[j].append(i)

used = [False] * N
dfs(start)
print("No")