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
cnt = [0] * (N + 1)
for i in range(2, N + 1):
    if cnt[i] >= 1:
        continue
    j = i
    while j <= N:
        cnt[j] += 1
        j += i
ans = 0
for i in range(1, N + 1):
    if cnt[i] >= K:
        ans += 1
print(ans)