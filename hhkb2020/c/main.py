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
P = na()
start = 0
MAX = 200001
S = set()
for p in P:
    S.add(p)
    if start == p:
        for i in range(start + 1, MAX):
            if i not in S:
                start = i
                break
    print(start)