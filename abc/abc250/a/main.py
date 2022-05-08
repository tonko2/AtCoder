import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W = na()
R, C = na()
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
ans = 0
for i in range(4):
    ny = R + dy[i]
    nx = C + dx[i]
    if ny >= 1 and nx >= 1 and nx <= W and ny <= H:
        ans += 1
print(ans)