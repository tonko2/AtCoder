import heapq
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

Q = ni()
d = defaultdict(int)
q = []
q2 = []
heapq.heapify(q)
heapq.heapify(q2)
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        d[x] += 1
        heapq.heappush(q, x)
        heapq.heappush(q2, -x)
    if query[0] == "2":
        x = int(query[1])
        c = int(query[2])
        d[x] = d[x] - min(d[x], c)
    if query[0] == "3":
        x = -1
        x2 = -1
        while q:
            x = heapq.heappop(q)
            if d[x] == 0:
                continue
            else:
                heapq.heappush(q, x)
                break
        while q2:
            x2 = -(heapq.heappop(q2))
            if d[x2] == 0:
                continue
            else:
                heapq.heappush(q2, -x2)
                break
        print(x2 - x)
