import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = list(ns())
Q = ni()
flag = 0
for _ in range(Q):
    t, a, b = na()
    a -= 1
    b -= 1
    if t == 1:
        if flag:
            if a < N and b < N:
                S[a + N], S[b + N] = S[b + N], S[a + N]
            elif N <= a and N <= b:
                S[a - N], S[b - N] = S[b - N], S[a - N]
            else:
                S[a + N], S[b - N] = S[b - N], S[a + N]
        else:
            S[a], S[b] = S[b], S[a]
    else:
        flag = 1 - flag
if flag:
    S = S[N:] + S[0:N]
print("".join(S))