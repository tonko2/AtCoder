import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, C, K = na()
T = [ni() for _ in range(N)]
T.sort()
ans = 0
t = 0
c = 0
for i in range(N):
    if c == 0:
        c += 1
        t = T[i]
    elif T[i] - t <= K:
        c += 1
    else:
        c = 1
        ans += 1
        t = T[i]
    if c == C:
        c = 0
        t = 0
        ans += 1
if c:
    ans += 1
print(ans)