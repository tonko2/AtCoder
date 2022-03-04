import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ni()
A = []
K = ni()
while S:
    A.append(S % 10)
    S //= 10
A.reverse()

for i in range(min(len(A), K)):
    if A[i] != 1:
        print(A[i])
        exit()
print(1)