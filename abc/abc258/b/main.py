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

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def dfs(x, y, z, cnt, digit):
    global ans
    if cnt == N:
        ans = max(ans, int(digit))
        return
    nx = x + dx[z]
    ny = y + dy[z]
    if nx == -1:
        nx = N - 1
    if ny == -1:
        ny = N - 1
    if nx == N:
        nx = 0
    if ny == N:
        ny = 0
    dfs(nx, ny, z, cnt + 1, digit + A[ny][nx])

ans = 0
N = ni()
A = []
for _ in range(N):
    A.append(ns())
for i in range(N):
    for j in range(N):
        for k in range(8):
            dfs(j, i, k, 1, A[i][j])
print(ans)