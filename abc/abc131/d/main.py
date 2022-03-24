import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
BA = []
for i in range(N):
    a, b = na()
    BA.append((b, a))
BA.sort()
cur = 0
for b, a in BA:
    if cur + a > b:
        print("No")
        exit()
    cur += a
print("Yes")