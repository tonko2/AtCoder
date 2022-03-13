import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, Q = na()
A = na()
B = [0] * (N + 1)
ans = 0
for i in range(N - 1):
    B[i + 1] = A[i + 1] - A[i]
    ans += abs(B[i + 1])

for i in range(Q):
    l, r, v = na()
    a = abs(B[l - 1]) + abs(B[r])
    if l > 1:
        B[l - 1] += v
    if r < N:
        B[r] -= v
    b = abs(B[l - 1]) + abs(B[r])
    ans += b - a
    print(ans)