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
S = [ns() for _ in range(N)]

dd = []
for i in range(N):
    d = defaultdict(int)
    for c in S[i]:
        d[c] += 1
    dd.append(d)

ans = []
for i in range(26):
    c = chr(ord('a') + i)
    min_v = INF
    for j in range(N):
        d = dd[j]
        min_v = min(min_v, d[c])
    ans.append(c * min_v)

print("".join(ans))


