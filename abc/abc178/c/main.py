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

def powmod(x, y):
    res = 1
    for i in range(y):
        res = (res * x) % MOD
    return res
N = ni()
print((powmod(10, N) - powmod(9, N) - powmod(9, N) + powmod(8, N)) % MOD)
