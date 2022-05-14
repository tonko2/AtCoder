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
A = na()

ans = ""
for i, s in enumerate(S):
    if i in A:
        ans += "\""
    ans += s
if A[-1] == len(S):
    ans += "\""
print(ans)