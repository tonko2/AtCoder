import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()

A.sort()
ans = 0
for i in range(N):
    ans += A[3 * N - (2 + 2 * i)]
print(ans)