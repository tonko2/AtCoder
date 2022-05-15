import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

W = ni()
if W == 1:
    print(1)
    exit()

A = []
N = W // 2
for i in range(1, N + 1):
    A.append(i)
print(*A)

A = [2, 3, 5, 7, 11, 13]

S = set()
for i in range(N):
    if A[i] <= W:
        S.add(A[i])
for i in range(N):
    for j in range(i + 1, N):
        if A[i] + A[j] <= W:
            S.add(A[i] + A[j])
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] <= W:
                S.add(A[i] + A[j] + A[k])

print(len(S))
