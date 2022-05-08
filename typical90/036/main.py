import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, Q = na()
X = [0] * N
Y = [0] * N
min_X = INF
max_X = -INF
min_Y = INF
max_Y = -INF
for i in range(N):
    X[i], Y[i] = na()
    X[i], Y[i] = X[i] + Y[i], Y[i] - X[i]
    min_X = min(min_X, X[i])
    max_X = max(max_X, X[i])
    min_Y = min(min_Y, Y[i])
    max_Y = max(max_Y, Y[i])

for i in range(Q):
    q = ni()
    q -= 1
    x1 = abs(X[q] - min_X)
    x2 = abs(X[q] - max_X)
    y1 = abs(Y[q] - min_Y)
    y2 = abs(Y[q] - max_Y)
    print(max(x1, x2, y1, y2))