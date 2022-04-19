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

cur = 0
cnt = 0
ans = 0
d = defaultdict(int)
for i in range(N):
    while cur < N:
        if d[A[cur]] == 0 and cnt == K:
            break
        if d[A[cur]] == 0:
            cnt += 1
        d[A[cur]] += 1
        cur += 1
    ans = max(ans, cur - i)
    if d[A[i]] == 1:
        cnt -= 1
    d[A[i]] -= 1
print(ans)