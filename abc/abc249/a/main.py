import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

T_d = 0
A_d = 0
A, B, C, D, E, F, X = na()

a = 0
while a < X:
    a += A
    T_d += A
    if a > X:
        T_d -= a - X
    a += C
T_d *= B

d = 0
while d < X:
    d += D
    A_d += D
    if d > X:
        A_d -= d - X
    d += F
A_d *= E

if T_d == A_d:
    print("Draw")
elif T_d > A_d:
    print("Takahashi")
else:
    print("Aoki")

