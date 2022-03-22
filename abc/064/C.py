import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
color = set()
free = 0
for a in A:
    if a >= 3200:
        free += 1
    else:
        if 1 <= a <= 399:
            color.add(1)
        if 400 <= a <= 799:
            color.add(2)
        if 800 <= a <= 1199:
            color.add(3)
        if 1200 <= a <= 1599:
            color.add(4)
        if 1600 <= a <= 1999:
            color.add(5)
        if 2000 <= a <= 2399:
            color.add(6)
        if 2400 <= a <= 2799:
            color.add(7)
        if 2800 <= a <= 3199:
            color.add(8)
print(max(len(color), 1), len(color) + free)
