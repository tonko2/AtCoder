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

a, b, d = na()
rad = math.radians(d)
print(math.cos(rad) * a - math.sin(rad) * b, math.sin(rad) * a + math.cos(rad) * b)