import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M, X = na()
ans = INF

C = []
A = []
for i in range(N):
    tmp = na()
    C.append(tmp[0])
    A.append(tmp[1:])

for bit in range(1 << N):
    money = 0
    tmp_M = [0] * M
    for i in range(N):
        if bit & 1 << i:
            money += C[i]
            for j in range(M):
                tmp_M[j] += A[i][j]
    flag = True
    for i in range(M):
        if tmp_M[i] < X:
            flag = False
    if flag:
        ans = min(ans, money)
if ans == INF:
    print(-1)
else:
    print(ans)