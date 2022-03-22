import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
N = len(S) + 1

A = [0] * N
B = [0] * N

for i in range(1, N):
    if S[i - 1] == "<":
        A[i] = A[i - 1] + 1
for i in range(N - 1)[::-1]:
    if S[i] == ">":
        B[i] = B[i + 1] + 1
C = [max(A[i], B[i]) for i in range(N)]
print(sum(C))