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
A = na()
res = 0
S = set()
for i in range(N):
    if i in S:
        continue
    if i == 0:
        if A[i] < A[N - 1]:
            res += A[i]
            S.add(i + 1)
        else:
            res += A[N - 1]
            S.add(N - 1)
    else:
        if A[i] < A[i - 1]:
            res += A[i]
            S.add(i + 1)
        else:
            res += A[i - 1]
    S.add(i)
    print(f'S = {S}, res = {res}')
print(res)

res = 0
for i in range(N):
    if i in S:
        continue
    if i == 0:
        if A[i] < A[N - 1]:
            res += A[i]
            S.add(i + 1)
        else:
            res += A[N - 1]
            S.add(N - 1)
    else:
        if A[i] < A[i - 1]:
            res += A[i]
            S.add(i + 1)
        else:
            res += A[i - 1]
    S.add(i)
    print(f'S = {S}, res = {res}')