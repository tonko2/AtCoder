import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B = na()
P = na()
Q = na()
bowl_idx = [7,8,9,0,4,5,6,2,3,1]
result = [[0] * 7 for _ in range(4)]
idx = 0
for i in range(4):
    j = i
    cnt = 0
    while cnt < 4 - i:
        bowl = bowl_idx[idx]
        if bowl in P:
            result[i][j + cnt * 2] = 1
        elif bowl in Q:
            result[i][j + cnt * 2] = 2
        else:
            result[i][j + cnt * 2] = -1
        idx += 1
        cnt += 1

for i in range(4):
    str = ""
    for j in range(7 - i):
        if result[i][j] == -1:
            str += "x"
        if result[i][j] == 0:
            str += " "
        if result[i][j] == 1:
            str += "."
        if result[i][j] == 2:
            str += "o"
    print(str)
