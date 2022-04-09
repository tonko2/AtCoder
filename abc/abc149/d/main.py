import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
R, S, P = na()
T = ns()
points = []
hands = []
for i in range(N):
    point = 0
    c = 0
    if T[i] == 'r':
        point = P
        c = 1
    if T[i] == 's':
        point = R
        c = 2
    if T[i] == 'p':
        point = S
        c = 3
    points.append(point)
    hands.append(c)

i = 0
while i < N:
    while i + K < N and hands[i] == hands[i + K]:
        points[i + K] = 0
        hands[i + K] = 0
        i += 1
    i += 1

print(sum(points))
