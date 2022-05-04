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
AB = []
for _ in range(N):
    a, b = na()
    AB.append((a, b))
AB.sort()
i = 0
now = K
pos = AB[0][0]
while i < N and now >= pos:
    now += AB[i][1]
    i += 1
    if i != N:
        pos = AB[i][0]
print(now)