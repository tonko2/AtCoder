import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B, C, X = na()
if A >= X:
    print(1)
elif A <= X <= B:
    print(C / (B - A))
else:
    print(0)