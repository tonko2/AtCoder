import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

a, b, c = na()
if c - b - a >= 0 and 4 * a * b < (c - a - b) ** 2:
    print("Yes")
else:
    print("No")