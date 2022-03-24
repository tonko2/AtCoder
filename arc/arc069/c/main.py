import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
ans = min(N, M // 2)
N, M = N - min(N, M // 2), M - min(2 * N, M)
ans += M // 4
print(ans)