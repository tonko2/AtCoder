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
ans = INF
for bit in range(1 << N):
    S = []
    for i in range(N):
        if bit & 1 << i:
            S.append(i)
    if len(S) != K:
        continue
    diff = 0
    initial = A[0]
    now = A[0]
    for i in range(S[0] + 1):
        now = max(now, A[i])
    diff = now - initial
    for i in range(1, len(S)):
        if now + 1 > A[S[i]]:
            diff += (now + 1) - A[S[i]]
        now = max(now + 1, A[S[i]])
    ans = min(ans, diff)
print(ans)