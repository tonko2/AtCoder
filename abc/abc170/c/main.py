import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

X, N = na()
P = na()
ans = 0
min_diff = INF
for i in range(-1, 102):
    if i in P:
        continue
    diff = abs(X - i)
    if min_diff > diff:
        min_diff = min(min_diff, diff)
        ans = i
print(ans)