import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, L = na()
S = ns()
cur = 1
ans = 0
for s in S:
    if s == '+':
        cur += 1
    if s == '-':
        cur -= 1
    if cur > L:
        cur = 1
        ans += 1
print(ans)