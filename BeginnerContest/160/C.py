import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

K, N = na()
A = na()
max_l = 0
total = 0
for i in range(N - 1):
    max_l = max(max_l, A[i + 1] - A[i])
    total += A[i + 1] - A[i]
print(K - max(max_l, K - total))
