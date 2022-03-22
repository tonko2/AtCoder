import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def check(a, b):
    while a and b:
        c, d = a % 10, b % 10
        if c + d >= 10:
            return False
        a //= 10
        b //= 10
    return True

N = ni()
A = na()
L = 6
S = 10 ** 6
dp = [0] * (S + 1)
for a in A:
    dp[a] += 1
for i in range(L):
    w = 10 ** i
    for j in range(S):
        if j // w % 10 < 9:
            dp[j + w] += dp[j]

ans = 0
for a in A:
    ans += dp[S - 1 - a]
    if check(a, a):
        ans -= 1
print(ans // 2)
