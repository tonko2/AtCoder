import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, Q = na()
S = ns()
total = [0] * (N + 1)
for i in range(N - 1):
    if S[i] == 'A' and S[i + 1] == 'C':
        total[i + 1] = total[i] + 1
    else:
        total[i + 1] = total[i]

for _ in range(Q):
    l, r = na()
    l -= 1
    r -= 1
    print(total[r] - total[l])