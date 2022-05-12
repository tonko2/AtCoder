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
d = defaultdict(int)
for i, a in enumerate(A):
    d[a] = i + 1
a = 0
b = 0
for i in range(len(A) // 2):
    a = max(a, A[i])
for i in range(len(A) // 2, len(A)):
    b = max(b, A[i])
print(d[min(a, b)])
