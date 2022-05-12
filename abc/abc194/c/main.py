import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
d = defaultdict(int)
for i in range(N):
    A[i] += 1000
    d[A[i]] += 1

ans = 0
keys = list(d.keys())
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        n = d[keys[i]]
        n2 = d[keys[j]]
        if keys[i] == keys[j]:
            n2 -= 1
        ans += ((keys[i] - keys[j]) ** 2) * (n * n2)
print(ans)