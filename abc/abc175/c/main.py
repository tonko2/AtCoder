import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

X, K, D = na()
if X < 0:
    X = -X
move = min(X // D, K)
X -= move * D
K -= move
if K % 2 == 0:
    print(X)
else:
    print(abs(X - D))

