import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W, N = na()
A = [0] * N
B = [0] * N

AB = []
BA = []
for i in range(N):
    A[i], B[i] = na()
    AB.append((A[i], B[i], i))
    BA.append((B[i], A[i], i))

AB.sort()
BA.sort()

pre = 0
diff = 0
for i in range(N):
    x, _, idx = AB[i]
    diff += max(0, x - pre - 1)
    A[idx] -= diff
    pre = x

pre = 0
diff = 0
for i in range(N):
    y, _, idx = BA[i]
    diff += max(0, y - pre - 1)
    B[idx] -= diff
    pre = y

for i in range(N):
    print(A[i], B[i])