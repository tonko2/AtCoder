import bisect
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def prime_factor(x):
    res = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            res.append(i)
            if x // i != i:
                res.append(x // i)
    return res
K = ni()
p = sorted(prime_factor(K))
N = len(p)
ans = 0
for i in range(N):
    for j in range(i, N):
        if K % (p[i] * p[j]) != 0:
            continue
        if p[j] <= (K // (p[i] * p[j])):
            ans += 1
print(ans)