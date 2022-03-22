import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()

ans = 0
for i in range(1, N + 1):
    for j in range(100):
        if i * (2 ** j) >= K:
            ans += (1 / N) * (0.5 ** j)
            break
print(ans)