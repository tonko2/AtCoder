import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def g1(x):
    return int("".join(sorted(str(x))[::-1]))

def g2(x):
    return int("".join(sorted(str(x))))

def f(x):
    return g1(x) - g2(x)

N, K = na()
for _ in range(K):
    N = f(N)
print(N)