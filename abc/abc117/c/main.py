import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
X = na()
S = []
X.sort()
for i in range(M - 1):
    S.append(abs(X[i] - X[i + 1]))
S.sort()
if N >= M:
    print(0)
else:
    print(sum(S[0:(M-1)-(N-1)]))