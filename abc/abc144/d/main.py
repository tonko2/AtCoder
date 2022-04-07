import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

a, b, x = na()
half = a * a * b * 0.5
if x > half:
    theta = math.atan((2 * (a * a * b - x)) / (a * a * a))
    print(theta / math.pi * 180)
else:
    theta = math.atan(a * (b * b) / (2 * x))
    print(theta / math.pi * 180)