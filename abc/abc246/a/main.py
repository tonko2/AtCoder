import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

dx = defaultdict(int)
dy = defaultdict(int)
for i in range(3):
    x, y = na()
    dx[x] += 1
    dy[y] += 1
ansx = -1
ansy = -1
for key in dx.keys():
    if dx[key] == 1:
        ansx = key
for key in dy.keys():
    if dy[key] == 1:
        ansy = key

print(ansx, ansy)