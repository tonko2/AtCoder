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
for i in range(N):
    X[i], Y[i] = na()
X.sort()
Y.sort()
xm = X[N // 2]
ym = Y[N // 2]
ans = 0
for i in range(N):
    ans += abs(X[i] - xm) + abs(Y[i] - ym)
print(ans)