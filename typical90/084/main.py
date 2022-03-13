import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = ns()
total = N * (N + 1) // 2
i = 0
while i < N:
    cnt = 1
    while i + 1 < N and S[i] == S[i + 1]:
        cnt += 1
        i += 1
    total -= cnt * (cnt + 1) // 2
    i += 1
print(total)