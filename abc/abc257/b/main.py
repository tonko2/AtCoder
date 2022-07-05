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

N, K, Q = na()
A = na()
L = na()
board = [0] * N
for i in range(K):
    board[A[i] - 1] = i + 1
for i in range(Q):
    cnt = 0
    for j in range(N):
        pos = j
        koma = board[j]
        if koma:
            cnt += 1
        if cnt == L[i] and j != N - 1:
            if board[pos + 1] == 0:
                board[pos + 1] = koma
                board[pos] = 0
            break
ans = []
for i in range(N):
    if board[i]:
        ans.append(i + 1)
print(*ans)