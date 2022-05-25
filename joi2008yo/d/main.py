import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

M = ni()
X = [0] * M
Y = [0] * M
for i in range(M):
    X[i], Y[i] = na()
N = ni()
dx = set()
dy = set()
for i in range(N):
    x, y = na()
    dx.add(x)
    dy.add(y)

candidate_x = set()
for i in range(1000001):
    flag1 = True
    for j in range(M):
        x, _ = X[j], Y[j]
        if not (x + i) in dx:
            flag1 = False
            break
    if flag1:
        candidate_x.add(i)

    flag2 = True
    for j in range(M):
        x, _ = X[j], Y[j]
        if not (x - i) in dx:
            flag2 = False
            break
    if flag2:
        candidate_x.add(-i)

candidate_y = set()

for i in range(1000001):
    flag1 = True
    for j in range(M):
        _, y = X[j], Y[j]
        if not (y + i) in dy:
            flag1 = False
            break
    if flag1:
        candidate_y.add(i)

    flag2 = True
    for j in range(M):
        _, y = X[j], Y[j]
        if not (y - i) in dy:
            flag2 = False
            break
    if flag2:
        candidate_y.add(-i)

for x in candidate_x:
    for y in candidate_y:
        flag = True
        for i in range(M):
            if not (X[i] + x in dx and Y[i] + y in dy):
                flag = False
                break
        if flag:
            print(x, y)
            exit()
