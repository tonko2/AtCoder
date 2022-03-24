import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
A.sort()
A.reverse()
d = defaultdict(int)
for a in A:
    d[a] += 1
ans_a = 0
ans_b = 0
for a in A:
    if d[a] >= 2:
        d[a] -= 2
        ans_a = a
        break
for a in A:
    if d[a] >= 2:
        ans_b = a
        break
print(ans_a * ans_b)

