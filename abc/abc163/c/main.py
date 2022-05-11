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
d = defaultdict(int)
A = na()
for i, a in enumerate(A):
    d[a] += 1
for i in range(N):
    print(d[i + 1])