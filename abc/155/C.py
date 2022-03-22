import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
d = defaultdict(int)
for _ in range(N):
    s = ns()
    d["".join(s)] += 1

max_cnt = 0
for s in d.keys():
    max_cnt = max(max_cnt, d[s])

ans = []
for s in d.keys():
    if max_cnt == d[s]:
        ans.append(s)
ans.sort()
for s in ans:
    print(s)