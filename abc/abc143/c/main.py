import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = ns()
ans = 0
i = 0
while i < N:
    c = S[i]
    while i + 1 < N and c == S[i + 1]:
        i += 1
    i += 1
    ans += 1
print(ans)