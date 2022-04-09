import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def prime_factors(n):
    rem = n
    res = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while rem % i == 0:
            rem //= i
            res.append(i)
    if rem != 1:
        res.append(rem)
    return res

N, P = na()
p = prime_factors(P)
d = defaultdict(int)
for a in p:
    d[a] += 1
ans = 1
for key in d.keys():
    for i in range(d[key] // N):
        ans *= key
print(ans)

