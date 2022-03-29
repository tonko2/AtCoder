import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def factorial(x):
    res = 1
    for i in range(2, x + 1):
        res = (res * i) % MOD
    return res

N, M = na()
if abs(N - M) > 1:
    print(0)
else:
    if N == M:
        print((factorial(N) * factorial(M) % MOD) * 2 % MOD)
    else:
        print(factorial(N) * factorial(M) % MOD)