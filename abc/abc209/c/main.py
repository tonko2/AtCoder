import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def p(a, b):
    if a < b:
        return 0
    res = 1
    for i in range(b):
        res = (res * (a - i)) % MOD
    return res

N = ni()
C = na()
C.sort()
ans = 1
d = defaultdict(int)
for i in range(N):
    d[C[i]] += 1
prev = 0
for key in d.keys():
    ans = (ans * p(key - prev, d[key])) % MOD
    prev += d[key]
print(ans)