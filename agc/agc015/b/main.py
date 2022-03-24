import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
N = len(S)
ans = 0
for i in range(N):
    if S[i] == 'U':
        ans += N - i - 1
        ans += 2 * i
    if S[i] == 'D':
        ans += i
        ans += 2 * (N - i - 1)

print(ans)