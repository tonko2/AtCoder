import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
d = defaultdict(int)
for i in range(M):
    a, b = na()
    if a == 1:
        if d[b] == 1:
            print("POSSIBLE")
            exit()
        else:
            d[b] = 1
    if b == N:
        if d[a] == 1:
            print("POSSIBLE")
            exit()
        else:
            d[a] = 1
print("IMPOSSIBLE")