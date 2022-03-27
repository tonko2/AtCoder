import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
total = [0] * (N + 1)
for i in range(N):
    total[i + 1] = total[i] + A[i]

ans = INF
for i in range(N - 1):
    ans = min(ans, abs(total[i + 1] - (total[N] - total[i + 1])))
print(ans)