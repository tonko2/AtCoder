import sys
from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 998244353
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

@lru_cache(maxsize=None)
def calc(x):
    if x <= 4:
        return x
    y = x // 2
    z = -(-x // 2)
    return calc(y) * calc(z) % MOD
X = ni()

print(calc(X))