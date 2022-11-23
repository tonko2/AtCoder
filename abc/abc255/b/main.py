import sys
import math
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

n, k = na()
A = na()
X = []
Y = []
for _ in range(n):
    x, y = na()
    X.append(x)
    Y.append(y)

candidate = []
for i in range(n):
    x = X[i]
    y = Y[i]
    minD = INF
    for j in range(k):
        x2 = X[A[j] - 1]
        y2 = Y[A[j] - 1]
        # if j + 1 in A:
        #     continue
        dis = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
        minD = min(minD, dis)
    candidate.append(minD)
print(max(candidate))