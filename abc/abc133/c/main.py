import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 2019

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

L, R = na()
ans = INF
for i in range(L, min(R, L + 2020)):
    for j in range(i + 1, min(R + 1, L + 2020)):
        ans = min(ans, i * j % MOD)
print(ans)