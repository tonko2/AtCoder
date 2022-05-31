import bisect
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
P = []
for _ in range(N):
    P.append(ni())
P2 = [0]
for i in range(N):
    P2.append(P[i])
for i in range(N):
    for j in range(N):
        P2.append(P[i] + P[j])
P2.sort()
ans = 0
for i in range(len(P2)):
    if M - P2[i] < 0:
        continue
    idx = bisect.bisect_right(P2, M - P2[i])
    ans = max(ans, P2[i] + P2[idx - 1])
print(ans)