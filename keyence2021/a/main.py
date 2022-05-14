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
B = na()
A_max = [0] * (N + 1)
B_max = [0] * (N + 1)
ans = 0
for i in range(N):
    A_max[i + 1] = max(A_max[i], A[i])
for i in range(N):
    print(max(ans, A_max[i + 1] * B[i]))
    ans = max(ans, A_max[i + 1] * B[i])