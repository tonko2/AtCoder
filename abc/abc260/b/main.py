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

N, X, Y, Z = na()
A = na()
B = na()
A_with_idx = []
B_with_idx = []
AB_with_idx = []
for i in range(N):
    A_with_idx.append((A[i], -i))
    B_with_idx.append((B[i], -i))
    AB_with_idx.append((A[i] + B[i], -i))
A_with_idx = sorted(A_with_idx)[::-1]
B_with_idx = sorted(B_with_idx)[::-1]
AB_with_idx = sorted(AB_with_idx)[::-1]

# print(A_with_idx)
# print(B_with_idx)
# print(AB_with_idx)

d = defaultdict(int)
ans = []
for i in range(N):
    if X == 0:
        break
    v, idx = A_with_idx[i]
    idx = -idx
    if d[idx] != 0:
        continue
    d[idx] = 1
    ans.append(idx + 1)
    X -= 1

for i in range(N):
    if Y == 0:
        break
    v, idx = B_with_idx[i]
    idx = -idx
    if d[idx] != 0:
        continue
    d[idx] = 1
    ans.append(idx + 1)
    Y -= 1

for i in range(N):
    if Z == 0:
        break
    v, idx = AB_with_idx[i]
    idx = -idx
    if d[idx] != 0:
        continue
    d[idx] = 1
    ans.append(idx + 1)
    Z -= 1

ans.sort()
for x in ans:
    print(x)
