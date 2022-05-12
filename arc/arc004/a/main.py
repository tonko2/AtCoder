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
ans = 0
X = []
Y = []
for _ in range(N):
    x, y = na()
    X.append(x)
    Y.append(y)
for i in range(N):
    for j in range(i + 1, N):
        x, y = X[i], Y[i]
        x2, y2 = X[j], Y[j]
        ans = max(ans, math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2))
print(ans)