import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B, C, K = na()

ans = 0
if K % 2 == 0:
    ans = A - B
else:
    ans = B - A

if abs(ans) > 10 ** 18:
    print("Unfair")
else:
    print(ans)