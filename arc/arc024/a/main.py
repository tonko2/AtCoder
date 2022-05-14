import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

L, R = na()
l = na()
r = na()
d_l = defaultdict(int)
d_r = defaultdict(int)
ans = 0
for ll in l:
    d_l[ll] += 1
for rr in r:
    d_r[rr] += 1
for ll in l:
    ans += min(d_l[ll], d_r[ll])
    d_l[ll] = 0
    d_r[ll] = 0
print(ans)