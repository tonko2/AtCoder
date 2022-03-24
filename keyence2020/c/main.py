import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K, S = na()
ans = []
for i in range(K):
    ans.append(S)
for i in range(N - K):
    if S == 10 ** 9:
        ans.append(S - 1)
    else:
        ans.append(S + 1)
print(*ans)