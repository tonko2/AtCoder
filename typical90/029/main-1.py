import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

W, N = na()
A = [0] * W
L = [0] * N
R = [0] * N
for i in range(N):
    L[i], R[i] = na()

for i in range(N):
    l, r = L[i], R[i]
    l -= 1
    height = 0
    for j in range(l, r):
        height = max(height, A[j])
    height += 1
    for j in range(l, r):
        A[j] = height
    print(height)