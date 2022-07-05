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

def dfs(v, x):
    if visited[v]:
        return
    visited[v] = True
    for i in range(N):
        if P[v] * x >= abs(X[v] - X[i]) + abs(Y[v] - Y[i]):
            dfs(i, x)

def judge(x):
    for i in range(N):
        for j in range(N):
            visited[j] = False
        dfs(i, x)
        flag = True
        for j in range(N):
            if not visited[j]:
                flag = False
        if flag:
            return True
    return False
N = ni()
X = []
Y = []
P = []
for _ in range(N):
    x, y, p = na()
    X.append(x)
    Y.append(y)
    P.append(p)
ok = 10 ** 10
ng = -1
visited = [False] * N
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok)