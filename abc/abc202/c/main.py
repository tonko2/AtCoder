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
B = na()
C = na()
d_A = defaultdict(int)
for a in A:
    d_A[a] += 1
d_C = defaultdict(int)
for c in C:
    d_C[c] += 1
ans = 0
for i, b in enumerate(B):
    if d_A[b]:
        ans += d_A[b] * d_C[i + 1]
print(ans)
