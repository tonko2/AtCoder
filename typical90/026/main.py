import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(pos, cur):
    col[pos] = cur
    for path in g[pos]:
        if col[path] == -1:
            dfs(path, 1 - cur)
N = ni()
col = [-1] * N
g = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = na()
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)
dfs(0, 0)
A = []
B = []
for i in range(N):
    if col[i] == 0:
        A.append(i + 1)
    else:
        B.append(i + 1)
if len(A) >= len(B):
    print(*A[0:N//2])
else:
    print(*B[0:N//2])


