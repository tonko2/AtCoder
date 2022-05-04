import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
B = [0] * 200
for a in A:
    B[a % 200] += 1
ans = 0
for b in B:
    ans += (b * (b - 1)) // 2
print(ans)