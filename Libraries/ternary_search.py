import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def f(x):
    return x + P / math.pow(2, x / 1.5)

low = 0
high = 100
P = float(ns())
cnt = 500
while cnt > 0:
    c1 = (low * 2 + high) / 3
    c2 = (low + high * 2) / 3
    if f(c1) > f(c2):
        low = c1
    else:
        high = c2
    cnt -= 1
print(f(low))