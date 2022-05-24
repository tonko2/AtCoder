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
T = na()
A = [0] * N
A[0] = 1 << T[0]
for i in range(1, N):
    A[i] = A[i - 1] >> T[i]
    A[i] += 1
    if A[i] % 2 == 0:
        A[i] += 1
    A[i] <<= T[i]
print(A)
print(A[-1])