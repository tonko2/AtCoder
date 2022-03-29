import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

tmpS = ns()
N = len(tmpS)
S = []
i = 0
while i < N:
    S.append(tmpS[i])
    while i + 1 < N and tmpS[i] == tmpS[i + 1]:
        i += 1
    i += 1
print(len(S) - 1)
