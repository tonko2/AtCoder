import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = [ni() for _ in range(N)]
B = sorted(A)
for a in A:
    if B[N - 1] != a:
        print(B[N - 1])
    else:
        print(B[N - 2])
