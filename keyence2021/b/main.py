import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
B = [0] * (3 * (10 ** 5) + 1)
for a in A:
    B[a] += 1

ans = 0
for i in range(N + 1):
    K = min(K, B[i])
    ans += K
print(ans)