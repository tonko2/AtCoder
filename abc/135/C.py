import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
B = na()
total = sum(A)
for i in range(N):
    A[i], B[i] = A[i] - min(B[i], A[i]), B[i] - min(B[i], A[i])
    A[i + 1], B[i] = A[i + 1] - min(B[i], A[i + 1]), B[i] - min(B[i], A[i + 1])
print(total - sum(A))