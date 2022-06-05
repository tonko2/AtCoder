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
ans = 0
for i in range(1, N + 1):
    k = i
    d = 2
    while d * d <= k:
        while k % (d * d) == 0:
            k /= (d * d)
        d += 1
    d = 1
    while k * d * d <= N:
        ans += 1
        d += 1
print(ans)