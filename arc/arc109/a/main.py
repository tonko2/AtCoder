import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

a, b, x, y = na()
if a > b:
    a -= 1
ans = 0
ans += x
ans += abs(a - b) * min(y, 2 * x)
print(ans)
