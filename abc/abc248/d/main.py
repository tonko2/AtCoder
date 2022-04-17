import bisect
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
d = defaultdict(list)
for i, a in enumerate(A):
    d[a].append(i + 1)
Q = ni()
for i in range(Q):
    L, R, X = na()
    l = d[X]
    left = bisect.bisect_right(l, R)
    right = bisect.bisect_left(l, L)
    print(left - right)