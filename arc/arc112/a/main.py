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
    return x * (x + 1) // 2
T = ni()
for _ in range(T):
    l, r = na()
    if r - l < l:
        print(0)
    else:
        print(f(r - 2 * l + 1))