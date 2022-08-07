import sys
import math
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, X, Y = na()

def rec(level, is_red):
    if level == 1:
        if is_red:
            return 0
        else:
            return 1
    if is_red:
        return rec(level - 1, 1) + rec(level, 0) * X
    else:
        return rec(level - 1, 1) + rec(level - 1, 0) * Y

print(rec(N, 1))
