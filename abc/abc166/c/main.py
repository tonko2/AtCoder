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
H = na()
flag = [True] * N

for _ in range(M):
    a, b = na()
    a -= 1
    b -= 1
    if H[a] > H[b]:
        flag[b] = False
    elif H[a] < H[b]:
        flag[a] = False
    else:
        flag[a] = flag[b] = False

ans = 0
for i in range(N):
    if flag[i]:
        ans += 1
print(ans)