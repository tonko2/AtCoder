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
for _ in range(N):
    A = na()
    total = sum(A[0:4]) + A[-1] * 110 / 900
    ans = max(ans, total)
print(ans)