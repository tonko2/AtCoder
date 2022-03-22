import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
min_v = min(A)
ans = 0
for i in range(0, N, K - 1):
    if i + 1 < N and max(A[i:i+K]) != min_v:
        ans += 1
print(ans)
