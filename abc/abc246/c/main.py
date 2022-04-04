import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K, X = na()
A = na()
A.sort()
for i in range(N - 1, -1, -1):
    tmp = A[i] // X
    tmp_2 = K
    A[i] -= X * min(tmp, K)
    K -= min(tmp, tmp_2)

A.sort()
for i in range(N - 1, -1, -1):
    if K:
        A[i] = 0
        K -= 1

ans = sum(A)
print(ans)