import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
EPS = 1 / (10 ** 6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, va, vb, L = na()
for i in range(N):
    t = L / va
    L = vb * t
if abs(L - int(L)) < EPS:
    print(int(L))
else:
    print(L)