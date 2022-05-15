import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, W = na()
A = na()

ans = 0
S = set()
for i in range(N):
    if A[i] <= W:
        S.add(A[i])
        ans += 1
for i in range(N):
    for j in range(i + 1, N):
        if A[i] + A[j] <= W:
            S.add(A[i] + A[j])
            ans += 1
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] <= W:
                S.add(A[i] + A[j] + A[k])
                ans += 1
print(len(S))