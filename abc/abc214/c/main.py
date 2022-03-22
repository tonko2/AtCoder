import heapq
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = na()
T = na()

all = [(v, i) for i, v in enumerate(T)]
heapq.heapify(all)
ans = [INF] * N
while all:
    v, i = heapq.heappop(all)
    if ans[i] < v:
        continue
    ans[i] = v
    heapq.heappush(all, (v + S[i], (i + 1) % N))

for v in ans:
    print(v)