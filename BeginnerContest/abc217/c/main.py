import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
P = na()
Q = [0] * N
for i in range(N):
    Q[P[i] - 1] = i + 1
print(*Q)