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
X = [0] * N
Y = [0] * N
d = set()
for i in range(N):
    X[i], Y[i] = na()
    d.add((X[i], Y[i]))

ans = 0
for i in range(N):
    x, y = X[i], Y[i]
    for j in range(i + 1, N):
        x2, y2 = X[j], Y[j]
        vx = x2 - x
        vy = y2 - y
        if (x2-vy, y2+vx) in d and (x-vy, y+vx) in d:
            dis = (x2 - x) ** 2 + (y2 - y) ** 2
            ans = max(ans, dis)
print(ans)
