import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B, C, D = na()
if A * 60 + B > C * 60 + D:
    print("Aoki")
else:
    print("Takahashi")
