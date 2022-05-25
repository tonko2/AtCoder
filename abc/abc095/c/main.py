import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B, C, X, Y = na()
ans = 0
if (A + B) >= 2 * C:
    ans += min(X, Y) * (2 * C)
    X, Y = X - min(X, Y), Y - min(X, Y)
    if X:
        ans += min(X * A, 2 * C * X)
    else:
        ans += min(Y * B, 2 * C * Y)
else:
    ans += A * X + B * Y
print(ans)