import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def modpow(a, b, m):
    res = 1
    while b != 0:
        if b % 2 == 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

N, K = na()

if K == 1:
    if N == 1:
        print(1)
    else:
        print(0)
elif N == 1:
    print(K % MOD)
elif N == 2:
    print(K * (K - 1) % MOD)
else:
    print((K * (K - 1) * modpow(K - 2, N - 2, MOD)) % MOD)