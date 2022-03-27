import sys
from collections import defaultdict, deque
import math

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

N, M = na()
S = ns()
T = ns()
G = math.gcd(N, M)
NG = N // G
MG = M // G
for i in range(G):
    if S[NG * i] != T[MG * i]:
        print(-1)
        exit()
print(lcm([N, M]))