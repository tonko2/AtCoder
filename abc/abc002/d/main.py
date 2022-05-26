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
R = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = na()
    a -= 1
    b -= 1
    R[a][b] = 1
    R[b][a] = 1

ans = 0
for bit in range(1 << N):
    S = []
    for i in range(N):
        if bit & 1 << i:
            S.append(i)

    cnt =  0
    flag = True
    for i in range(len(S)):
        a = S[i]
        for j in range(i + 1, len(S)):
            b = S[j]
            if not (R[a][b] and R[b][a]):
                flag = False
                break
    if flag:
        ans = max(ans, len(S))
print(ans)