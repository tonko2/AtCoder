import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

d = defaultdict(int)
d["TAKAHASHIKUN"] = 1
d["Takahashikun"] = 1
d["takahashikun"] = 1

N = ni()
S = list(map(str, input().split()))
s = S[-1]
S.pop()
S.append(s[0:(len(s) - 1)])
ans = 0
for s in S:
    if d["".join(s)]:
        ans += 1
print(ans)