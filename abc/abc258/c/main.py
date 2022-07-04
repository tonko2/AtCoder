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

N, Q = na()
S = ns()
total = 0
for _ in range(Q):
    t, x = na()
    if t == 1:
        total += x
    else:
        x -= 1
        x = (x - total) % N
        print(S[x])