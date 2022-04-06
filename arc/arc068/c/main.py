import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

X = ni()
if X % 11 == 0 or (7 <= X % 11 <= 10):
    if X % 11 != 0:
        X += 11 - X % 11
    print(2 * (X // 11))
else:
    print(2 * (X // 11) + 1)
