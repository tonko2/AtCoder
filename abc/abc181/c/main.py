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

N = ni()
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = na()

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if cross(X[k] - X[j], Y[k] - Y[j], X[k] - X[i], Y[k] - Y[i]) == 0:
                print("Yes")
                exit()
print("No")