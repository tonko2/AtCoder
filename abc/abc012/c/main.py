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
diff = 2025 - N
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == diff:
            print(f'{i} x {j}')