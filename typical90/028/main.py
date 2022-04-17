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
lx = [0] * N
ly = [0] * N
rx = [0] * N
ry = [0] * N
cnt = [[0] * 1001 for _ in range(1001)]
for i in range(N):
    lx[i], ly[i], rx[i], ry[i] = na()

for i in range(N):
    cnt[lx[i]][ly[i]] += 1
    cnt[lx[i]][ry[i]] -= 1
    cnt[rx[i]][ly[i]] -= 1
    cnt[rx[i]][ry[i]] += 1

for i in range(1001):
    for j in range(1, 1001):
        cnt[i][j] += cnt[i][j - 1]

for i in range(1, 1001):
    for j in range(1001):
        cnt[i][j] += cnt[i - 1][j]

ans = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        if cnt[i][j] >= 1:
            ans[cnt[i][j]] += 1

for i in range(1, N + 1):
    print(ans[i])
