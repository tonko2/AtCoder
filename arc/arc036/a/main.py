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
T = [ni() for _ in range(N)]
for i in range(N - 2):
    total = T[i] + T[i + 1] + T[i + 2]
    if total < K:
        print(i + 3)
        exit()
print(-1)