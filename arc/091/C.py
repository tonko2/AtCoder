import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
if (N == 1 and M == 1) or (N == 1 and M == 2) or (N == 2 and M == 1):
    print(1)
elif N == 2 or M == 2:
    print(0)
else:
    print(max(1, N - 2) * max(1, M - 2))
