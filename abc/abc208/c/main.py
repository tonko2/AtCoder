import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
info = []
for i in range(N):
    info.append((A[i], i))
info.sort()
ans = [0] * N
for i in range(N):
    ans[i] = K // N
K %= N
for i in range(K):
    _, idx = info[i]
    ans[idx] += 1
for a in ans:
    print(a)