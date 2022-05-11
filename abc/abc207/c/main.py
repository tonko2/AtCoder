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
    if T[i] == 2:
        R[i] -= 0.5
    if T[i] == 3:
        L[i] += 0.5
    if T[i] == 4:
        R[i] -= 0.5
        L[i] += 0.5

ans = 0
for i in range(N):
    a = L[i]
    b = R[i]
    for j in range(i + 1, N):
        a2 = L[j]
        b2 = R[j]
        if a2 <= a <= b2 or a2 <= b <= b2 or a <= a2 <= b or a <= b2 <= b:
            ans += 1
print(ans)
