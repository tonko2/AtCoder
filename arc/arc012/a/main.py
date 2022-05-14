import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

D = ns()
d = defaultdict(int)
d["Monday"] = 5
d["Tuesday"] = 4
d["Wednesday"] = 3
d["Thursday"] = 2
d["Friday"] = 1
d["Saturday"] = 0
d["Sunday"] = 0
print(d["".join(D)])