import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

# 3角形の面積
def heron(x1, y1, x2, y2, x3, y3):

    def segment(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    AB = segment(x1, y1, x2, y2)
    BC = segment(x2, y2, x3, y3)
    CA = segment(x3, y3, x1, y1)
    s = (AB + BC + CA) / 2
    ss = s * (s - AB) * (s - BC) * (s - CA)
    if ss < 0:
        return -1
    return math.sqrt(s * (s - AB) * (s - BC) * (s - CA))

x1, y1, x2, y2, x3, y3 = na()
print(heron(x1, y1, x2, y2, x3, y3))