import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

N, K = na()
X = [0] * (N + 1)
Y = [0] * (N + 1)

for i in range(N):
    X[i], Y[i] = na()

if K == 1:
    print("Infinity")
    exit()

ans = set()
for i in range(N):
    for j in range(i + 1, N):
        x, y = X[i] - X[j], Y[i] - Y[j]
        coordinates = []
        if x == 0:
            for k in range(N):
                if X[i] == X[k]:
                    coordinates.append(k)
        else:
            for k in range(N):
                x1, y1 = X[i] - X[k], Y[i] - Y[k]
                if cross(x, y, x1, y1) == 0:
                    coordinates.append(k)
        if len(coordinates) >= K:
            ans.add(tuple(coordinates))
print(len(ans))