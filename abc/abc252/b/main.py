import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
B = na()
max_v = sorted(A)[-1]
A_idx = []
for i in range(N):
    if max_v == A[i]:
        A_idx.append(i + 1)

flag = True
for b in B:
    for idx in A_idx:
        if b == idx:
            flag = False
if flag:
    print("No")
else:
    print("Yes")
