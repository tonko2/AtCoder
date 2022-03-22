import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
A = na()
B = na()
d = defaultdict(int)
for a in A:
    d[a] += 1
for b in B:
    if d[b] > 0:
        d[b] -= 1
    else:
        print("No")
        exit()
print("Yes")
