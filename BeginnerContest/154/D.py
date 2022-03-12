import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
P = na()
ans = 0
arr = []
for i in range(N):
    n = (P[i] * (P[i] + 1)) // 2
    arr.append(n / P[i])
s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + arr[i]

ans = 0
for i in range(N - K + 1):
    ans = max(ans, s[i + K] - s[i])
print(ans)