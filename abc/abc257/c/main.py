import sys
import math
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = ns()
W = na()
A = []
ans = 0
for i in range(N):
    A.append((W[i], S[i]))
    if S[i] == '1':
        ans += 1
A.sort()
cur = ans
for i in range(N):
    if A[i][1] == '1':
        cur -= 1
    else:
        cur += 1
    if i < N - 1:
        if A[i][0] != A[i + 1][0]:
            ans = max(ans, cur)
    else:
        ans = max(ans, cur)
print(ans)