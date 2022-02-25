import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
X = na()
avg = sum(X) // N
total1 = 0
total2 = 0
for a in X:
    total1 += (a - avg) ** 2
for a in X:
    total2 += (a - (avg + 1)) ** 2
print(min(total1, total2))
