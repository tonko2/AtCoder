import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

d_l = defaultdict(list)
d_r = defaultdict(list)

N = ni()
X = [0] * N
Y = [0] * N
for i in range(N):
     X[i], Y[i] = na()
S = ns()
for i, c in enumerate(S):
    if c == 'R':
        d_r[Y[i]].append(X[i])
    else:
        d_l[Y[i]].append(X[i])

for key in d_r.keys():
    d_r[key].sort()

for key in d_l.keys():
    d_l[key].sort()

for i, c in enumerate(S):
    x, y = X[i], Y[i]
    if c == 'R':
        if len(d_l[y]) == 0:
            continue
        x2 = d_l[y][-1]
        if x < x2:
            print("Yes")
            exit()
    else:
        if len(d_r[y]) == 0:
            continue
        x2 = d_r[y][0]
        if x > x2:
            print("Yes")
            exit()

print("No")