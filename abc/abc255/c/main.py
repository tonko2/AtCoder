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

X, A, D, N = na()

if D < 0:
    A = A + (N - 1) * D
    D = -D

ans = INF
left = 1
right = N
while left <= right:
    mid = (left + right) // 2
    if A + (mid - 1) * D < X:
        left = mid + 1
    else:
        right = mid - 1
ans = INF
for i in range(max(1, left - 1), min(N + 1, left + 2)):
    s = A + (i - 1) * D
    ans = min(ans, abs(X - s))
print(ans)