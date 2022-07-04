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

N, X = na()
A = [0] * N
B = [0] * N
b_val = INF
total = 0
min_B = [INF] * N
total_AB = [0] * N
for i in range(N):
    A[i], B[i] = na()
    min_B[i] = min(b_val, B[i])
    b_val = min(b_val, B[i])
    total = total + A[i] + B[i]
    total_AB[i] = total
ans = INF
for i in range(min(N, X)):
    ans = min(ans, total_AB[i] + min_B[i] * (X - i - 1))
print(ans)
