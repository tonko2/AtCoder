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
cnt = 0
for i in range(1, 100000000):
    if 25 * i <= N:
        cnt += 1
    else:
        break
print(cnt)

