import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def f(x):
    return (x * (x + 1) // 2) % MOD

L, R = na()
ans = 0
for i in range(1, 20):
    vl = max(L, 10 ** (i - 1))
    vr = min(R, (10 ** i) - 1)
    print(vl, vr)
    if vl > vr:
        continue
    val = (f(vr) - f(vl - 1)) % MOD
    ans += i * val
    ans %= MOD
print(ans)
