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
ans = 0
comma = 0
L = 1
R = 10
for i in range(17):
    if i != 0 and i % 3 == 0:
        comma += 1
    if R <= N:
        ans += (R - L) * comma
    else:
        ans += (N - L + 1) * comma
        break
    L *= 10
    R *= 10
print(ans)