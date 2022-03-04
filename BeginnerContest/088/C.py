import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

X, Y = na()
cnt = 0
while X <= Y:
    X *= 2
    cnt += 1
print(cnt)