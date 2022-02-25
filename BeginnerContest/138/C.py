import heapq
import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
V = na()
heapq.heapify(V)
while len(V) > 1:
    a = heapq.heappop(V)
    b = heapq.heappop(V)
    heapq.heappush(V, (a + b) / 2)

print(V.pop())