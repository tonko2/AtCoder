import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

y = ni()
m = ni()
d = ni()
if m == 1:
    y -= 1
    m = 13
if m == 2:
    y -= 1
    m = 14
calc = 365 * y + y // 4 - y // 100 + y // 400 + (306 * (m + 1) // 10) + d - 429
print(735369 - calc)