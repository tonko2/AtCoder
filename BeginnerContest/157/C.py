import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
SC = []
for _ in range(M):
    s, c = na()
    SC.append((s, c))

start = 10 ** (N - 1) if N > 1 else 0
for i in range(start, 10 ** N):
    flag = True
    for s, c in SC:
        if (i // (10 ** (N - s))) % 10 != c:
            flag = False
    if flag:
        print(i)
        exit()
print(-1)
