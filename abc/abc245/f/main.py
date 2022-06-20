import sys
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
inc = [0] * N
out = [[] for _ in range(N)]
for _ in range(M):
    a, b = na()
    a -= 1
    b -= 1
    inc[a] += 1
    out[b].append(a)
ans = N
q = [i for i, c in enumerate(inc) if c == 0]
while q:
    ans -= 1
    v = heapq.heappop(q)
    s = len(out[v])
    for i in range(s):
        inc[out[v][i]] -= 1
        if inc[out[v][i]] == 0:
            heapq.heappush(q, out[v][i])
print(ans)