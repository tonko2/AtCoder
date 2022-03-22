import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K, Q = na()
A = [K - Q] * N
for _ in range(Q):
    a = ni()
    A[a - 1] += 1
for i in range(N):
    if A[i] > 0:
        print("Yes")
    else:
        print("No")