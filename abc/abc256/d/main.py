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
LR = []
for _ in range(N):
    l, r = na()
    LR.append((l, r))
LR.sort()
ans = []
L = LR[0][0]
R = LR[0][1]
for (l, r) in LR:
    if R >= r:
        continue
    if R >= l:
        R = r
    else:
        ans.append((L, R))
        R = r
        L = l
ans.append((L, R))
for (l, r) in ans:
    print(l, r)

