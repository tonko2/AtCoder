import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

a, b = na()
if a + 1 == b or a == 1 and b == 10:
    print("Yes")
else:
    print("No")