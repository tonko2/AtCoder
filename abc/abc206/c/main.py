import bisect
import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
ans = 0
d = defaultdict(list)
for i in range(N):
    d[A[i]].append(i)

for i in range(N):
    l = d[A[i]]
    ans += N - bisect.bisect_right(l, i) - i
print(ans)