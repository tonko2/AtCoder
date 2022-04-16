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
S = [[] for _ in range(N + 1)]
S[1].append(1)
for i in range(2, N + 1):
    tmp = S[i - 1]
    for a in tmp:
        S[i].append(a)
    S[i].append(i)
    for a in tmp:
        S[i].append(a)
print(*S[N])