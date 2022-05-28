import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, A, B = na()
S = N * (N + 1) // 2
a = ((N // A) * (N // A + 1) // 2) * A
b = ((N // B) * (N // B + 1) // 2) * B
c = A * B // (math.gcd(A, B))
d = ((N // c) * (N // c + 1) // 2) * c

if A == B:
    print(S - a)
else:
    print(S - a - b + d)