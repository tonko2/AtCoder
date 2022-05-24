import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, X = na()
S = ns()
up = 0
tmp_S = ""
for c in S[::-1]:
    if c == 'U':
        up += 1
    if c == 'L':
        if up:
            up -= 1
        else:
            tmp_S += c
    if c == 'R':
        if up:
            up -= 1
        else:
            tmp_S += c
tmp_S = 'U' * up + tmp_S[::-1]
S = tmp_S
for c in S:
    if c == 'L':
        X = 2 * X
    if c == 'R':
        X = 2 * X + 1
    if c == 'U':
        X //= 2
print(X)