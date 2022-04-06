import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
X = []
Y = []
bolls = [1] * (N + 1)
red = [False] * (N + 1)
red[1] = True
for _ in range(M):
    x, y = na()
    if red[x]:
        red[y] = True
        if bolls[x] == 1:
            red[x] = False
    bolls[x] -= 1
    bolls[y] += 1
cnt = 0
for i in range(1, N + 1):
    if red[i]:
        cnt += 1
print(cnt)


