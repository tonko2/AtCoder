import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

X = ni()
goods = [5, 4, 3, 2, 1]
x = X % 100
min_unit = 0
for a in goods:
    min_unit += x // a
    x %= a
if X >= min_unit * 100:
    print(1)
else:
    print(0)