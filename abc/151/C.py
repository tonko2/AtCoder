import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
WA = 0
d = dict()
d2 = defaultdict(int)
for _ in range(M):
    p, s = map(str, input().split())
    if s == "AC" and d.get((p, s), 0) == 0:
        d[(p, s)] = 1
        WA += d2[(p, "WA")]
    if s == "WA" and d.get((p, "AC"), 0) == 0:
        d2[(p, s)] += 1
print(len(d.keys()), WA)