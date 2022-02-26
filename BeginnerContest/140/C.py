import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
B = na()
A = [float('inf')] * N
for i in range(N - 1):
    A[i] = min(A[i], B[i])
    A[i + 1] = B[i]
print(sum(A))