import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = input().split()
d = defaultdict(str)
d["Left"] = "<"
d["Right"] = ">"
d["AtCoder"] = "A"
ans = [d[s] for s in S]
print(*ans)
