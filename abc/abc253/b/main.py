import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W = na()
grid = []
for _ in range(H):
    grid.append(ns())
c = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'o':
            c.append((i, j))
x, y = c[0]
x2, y2 = c[1]
print(abs(x - x2) + abs(y - y2))