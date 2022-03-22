import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B = na()
for i in range(1, 1001):
    if int(i * 0.08) == A and int(i * 0.10) == B:
        print(i)
        exit()
print(-1)