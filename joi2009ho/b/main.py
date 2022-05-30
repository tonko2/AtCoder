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

D = ni()
S = [0, D]
N = ni()
M = ni()
for i in range(N - 1):
    S.append(ni())
S.sort()
ans = 0
for _ in range(M):
    d = ni()
    idx = bisect.bisect_right(S, d)
    ans += min(abs(d - S[idx]), abs(d - S[idx - 1]))
print(ans)