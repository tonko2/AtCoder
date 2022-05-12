import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

ans = [0] * 10001
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            v = (i + j + k) ** 2 - (i * j + i * k + j * k)
            if v <= 10000:
                ans[v] += 1
N = ni()
for i in range(1, N + 1):
    print(ans[i])
