import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, L, W = na()
A = na()
cur = 0
ans = 0
for i in range(N):
    if cur < A[i]:
        sheets = -(-(A[i] - cur) // W)
        ans += sheets
    cur = A[i] + W
ans += -(-(L - cur) // W)
print(ans)