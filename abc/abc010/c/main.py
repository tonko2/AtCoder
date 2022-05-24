import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

sx, sy, gx, gy, T, V = na()
N = ni()
for _ in range(N):
    x, y = na()
    dis = math.sqrt((sx - x) ** 2 + (sy - y) ** 2)
    dis2 = math.sqrt((x - gx) ** 2 + (y - gy) ** 2)
    if T * V >= dis + dis2:
        print("YES")
        exit()
print("NO")
