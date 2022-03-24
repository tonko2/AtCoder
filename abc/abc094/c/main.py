import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
X = na()
tmp_X = X.copy()
X.sort()
mid_index = (N - 1) // 2
mid_avg = (X[mid_index] + X[mid_index + 1]) / 2
for a in tmp_X:
    if mid_avg <= a:
        print(X[mid_index])
    else:
        print(X[mid_index + 1])