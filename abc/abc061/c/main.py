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
AB = []
for i in range(N):
    a, b = na()
    AB.append((a, b))
AB.sort()
total = 0
for i in range(N):
    a, b = AB[i]
    total += b
    if K <= total:
        print(a)
        exit()