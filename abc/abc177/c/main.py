import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
imos = [0]
for a in A:
    imos.append(a + imos[-1])
ans = 0
for i in range(N - 1):
    ans = (ans + (A[i] * (imos[N] - imos[i + 1]))) % MOD
print(ans)