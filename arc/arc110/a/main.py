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

def lcm(A):
    res = A[0]
    N = len(A)
    for i in range(1, N):
        gcd = math.gcd(res, A[i])
        res = gcd * (res // gcd) * (A[i] // gcd)
    return res

N = ni()
ans = 1
A = []
for i in range(2, N + 1):
    A.append(i)
print(lcm(A) + 1)