import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A = na()
candidates = []
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            candidates.append(A[i] + A[j] + A[k])
candidates.sort()
print(candidates[-3])

