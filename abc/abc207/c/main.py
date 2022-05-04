import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
T = [0] * N
L = [0] * N
R = [0] * N
for i in range(N):
    T[i], L[i], R[i] = na()

for i in range(N):
    a = L[i]
    b = R[i]
    for j in range(i + 1, N):
