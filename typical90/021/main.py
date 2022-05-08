import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(pos):
    used[pos] = True
    for v in G[pos]:
        if used[v] == False:
            dfs(v)
    I.append(pos)

def dfs2(pos):
    global cnt
    used[pos] = True
    cnt += 1
    for v in H[pos]:
        if used[v] == False:
            dfs2(v)

N, M = na()
G = [[] for _ in range(N)]
H = [[] for _ in range(N)]

for i in range(M):
    a, b = na()
    a -= 1
    b -= 1
    G[a].append(b)
    H[b].append(a)

used = [0] * N
I = []
for i in range(N):
    if used[i] == False:
        dfs(i)

used = [0] * N
I.reverse()
cnt = 0
ans = 0

for i in I:
    if used[i]:
        continue
    cnt = 0
    dfs2(i)
    ans += cnt * (cnt - 1) // 2

print(ans)