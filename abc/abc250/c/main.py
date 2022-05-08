import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, Q = na()
A = []
d = defaultdict(int) # d[num] = index
di = defaultdict(int) # di[index] = num
for i in range(1, N + 1):
    A.append(i)
    d[i] = i - 1
    di[i - 1] = i

for _ in range(Q):
    x = ni()
    num_a = x
    idx = d[x]
    nxtIdx = idx + 1
    if idx + 1 == N:
        nxtIdx = idx - 1
    num_b = di[nxtIdx]
    A[idx], A[nxtIdx] = A[nxtIdx], A[idx]
    d[num_a], d[num_b] = d[num_b], d[num_a]
    di[idx], di[nxtIdx] = di[nxtIdx], di[idx]

print(*A)
