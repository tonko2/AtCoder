import math
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

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

A, B, C, D = na()
A_C = (A - 1) // C
A_D = (A - 1) // D
A_CD = (A - 1) // lcm([C, D])
B_C = B // C
B_D = B // D
B_CD = B // lcm([C, D])
ans = (B - A + 1) - (B_C - A_C) - (B_D - A_D) + (B_CD - A_CD)
print(ans)