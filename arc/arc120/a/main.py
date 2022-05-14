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
max_A = [0]
sum_A = [0]
sum_sum_A = [0]
for i in range(0, N):
    max_A.append(max(max_A[-1], A[i]))
    sum_A.append(sum_A[-1] + A[i])
    sum_sum_A.append(sum_sum_A[-1] + sum_A[i + 1])
for i in range(N):
    print(sum_sum_A[i + 1] + max_A[i + 1] * (i + 1))

