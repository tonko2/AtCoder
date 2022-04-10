import bisect
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
S = sum(A[0:K])
if sum(sorted(A)[::-1][0:K]) < S + 1:
    print(-1)
else:
    max_v = [0] * (N - K)
    max_v[0] = A[K]
    for i in range(1, N - K):
        max_v[i] = max(max_v[i - 1], A[i + K])
    ans = INF
    for i in range(K):
        idx = bisect.bisect_left(max_v, A[i] + 1)
        if idx != (N - K):
            left = K - i - 1
            right = idx + 1
            ans = min(ans, left + right)
    print(ans)
