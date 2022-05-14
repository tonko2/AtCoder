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
ans = 0
for i, s in enumerate(S):
    if i % 2 == 0:
        ans += int(s)
    else:
        ans -= int(s)
print(ans)