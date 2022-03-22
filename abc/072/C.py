import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
d = defaultdict(int)
for a in A:
    d[a] += 1
    d[a - 1] += 1
    d[a + 1] += 1

ans = 0
for a in d.keys():
    ans = max(ans, d[a])
print(ans)