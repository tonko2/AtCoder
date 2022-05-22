import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = na()
K = ni()
C = [0] * K
D = [0] * K
for i in range(K):
    C[i], D[i] = na()

ans = 0
for bit in range(1 << K):
    d = defaultdict(int)
    for i in range(K):
        if bit & 1 << i:
            d[C[i]] += 1
        else:
            d[D[i]] += 1
    cnt = 0
    for i in range(M):
        if d[A[i]] and d[B[i]]:
            cnt += 1
    ans = max(ans, cnt)
print(ans)