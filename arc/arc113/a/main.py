import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

K = ni()

ans = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        if i * j > K:
            break
        ans += K // (i * j)
print(ans)