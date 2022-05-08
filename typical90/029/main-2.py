import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A = [0] * 524288
W, N = na()
L = [0] * N
R = [0] * N
for i in range(N):
    L[i], R[i] = na()

A = []
for i in range(N):
    A.append(L[i])
    A.append(R[i])

B = sorted(set(A))

D = {v: i for i, v in enumerate(B)}

h = [0] * len(D)
for i in range(N):
    l, r = D[L[i]], D[R[i]]
    height = 0
    for j in range(l, r):
        height = max(height, A[j])
    height += 1
    for j in range(l, r):
        A[j] = height
    print(height)