import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
d = dict()
d["O"] = "0"
d["D"] = "0"
d["I"] = "1"
d["Z"] = "2"
d["S"] = "5"
d["B"] = "8"
ans = ""
for s in S:
    ans += d.get(s, s)
print(ans)
