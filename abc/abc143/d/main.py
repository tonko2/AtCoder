import bisect
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
L = na()

ans = 0
L.sort()
for i in range(N):
    for j in range(i + 1, N):
        ans += bisect.bisect_left(L, L[i] + L[j]) - 1 - j
print(ans)
