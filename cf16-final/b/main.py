import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def sigma(x):
    return x * (x + 1) // 2
N = ni()

m = 0
remain = 0
for i in range(1, N+1):
    total = sigma(i)
    if total >= N:
        m = i
        remain = total - N
        break
for i in range(1, m + 1):
    if remain == i:
        continue
    print(i)
