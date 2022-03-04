import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
red = 0
blue = 0
for c in S:
    if c == '0':
        red += 1
    else:
        blue += 1
print(2 * min(red, blue))