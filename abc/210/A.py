import sys
input = lambda: sys.stdin.readline().rstrip()

N, A, X, Y = map(int, input().split())

if N <= A:
    print(N * X)
else:
    print(X * A + (N - A) * Y)