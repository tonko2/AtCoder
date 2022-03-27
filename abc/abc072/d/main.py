import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
P = na()
ans = 0
i = 0
while i < N:
    cnt = 0
    while i < N and P[i] == i + 1:
        cnt += 1
        i += 1
    i += 1
    ans += -(-cnt // 2)
print(ans)