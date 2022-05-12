import itertools
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
T = []
paths = []
for i in range(N):
    T.append(na())
    if i == 0:
        continue
    paths.append(i)
ans = 0
for path in itertools.permutations(paths):
    cur = 0
    total = 0
    for p in path:
        total += T[cur][p]
        cur = p
    total += T[cur][0]
    if total == K:
        ans += 1
print(ans)