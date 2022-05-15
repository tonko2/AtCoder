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
S = []
T = []
d = defaultdict(int)
for _ in range(N):
    s, t = input().split()
    t = int(t)
    t += 10
    S.append(s)
    T.append(t)
    if d[s]:
        continue
    d[s] = t

ans = 1
ans_v = 0
for i in range(N):
    s, t = S[i], T[i]
    if ans_v < d[s]:
        ans_v = d[s]
        ans = i + 1
print(ans)
