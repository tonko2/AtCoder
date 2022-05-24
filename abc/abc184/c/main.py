import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

r1, c1 = na()
r2, c2 = na()

if r1 == r2 and c1 == c2:
    print(0)
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
    print(1)
elif (abs(r1 - r2) + abs(c1 - c2)) % 2 == 0:
    print(2)
elif abs(r1 - r2) + abs(c1 - c2) <= 6:
    print(2)
elif abs((r1 + c1) - (r2 + c2)) <= 3:
    print(2)
elif abs((r1 - c1) - (r2 - c2)) <= 3:
    print(2)
else:
    print(3)
