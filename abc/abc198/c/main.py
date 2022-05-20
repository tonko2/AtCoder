import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

R, X, Y = na()
d = math.sqrt(X * X + Y * Y)
if d < R:
    print(2)
else:
    print(math.ceil(d/R))