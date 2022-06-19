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
A = na()
ans = 0
B = []
for i in range(N):
    B.append(0)
    for j in range(len(B)):
        B[j] += A[i]
for i in range(N):
    if B[i] > 3:
        ans += 1
print(ans)