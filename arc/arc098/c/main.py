import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = ns()
W = [0] * (N + 1)
E = [0] * (N + 1)
for i, c in enumerate(S):
    W[i + 1] = W[i]
    E[i + 1] = E[i]
    if c == 'W':
        W[i + 1] += 1
    else:
        E[i + 1] += 1

ans = INF
for i in range(N):
    ans = min(ans, W[i + 1] + E[N] - E[i])
print(ans - 1)
