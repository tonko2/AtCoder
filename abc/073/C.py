import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

d = defaultdict(int)
N = ni()
for i in range(N):
    a = ni()
    if d[a] > 0:
        d[a] = 0
    else:
        d[a] = 1

ans = 0
for key in d.keys():
    if d[key] > 0:
        ans += 1
print(ans)