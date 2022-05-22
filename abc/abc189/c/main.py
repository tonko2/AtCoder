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
for i in range(N):
    min_v = A[i]
    for j in range(i, N):
        min_v = min(min_v, A[j])
        ans = max(ans, (j - i + 1) * min_v)
print(ans)