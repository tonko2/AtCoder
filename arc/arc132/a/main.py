import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

n = ni()
R = na()
C = na()
q = ni()
ans = []

for i in range(q):
    r, c = na()
    r, c = r - 1, c - 1
    ans.append('#' if R[r] + C[c] > n else '.')
print("".join(ans))