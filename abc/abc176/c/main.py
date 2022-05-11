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
ans = 0
for i in range(N - 1):
    diff = max(0, A[i] - A[i + 1])
    A[i + 1] += diff
    ans += diff
print(ans)