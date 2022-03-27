import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
d = defaultdict(int)
for a in A:
    d[a] += 1
ans = 0
for key in d.keys():
    if d[key] > key:
        ans += d[key] - key
    if d[key]< key:
        ans += d[key]
print(ans)