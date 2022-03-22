import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, T = na()
A = na()
ans = T
cur = 0
for i in range(1, N):
    ans += min(T, A[i] - cur)
    cur = A[i]

print(ans)