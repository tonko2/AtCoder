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
B = []
for i in range(N):
    B.append((A[i], i + 1))
B = sorted(B)[::-1]
for (_, idx) in B:
    print(idx)