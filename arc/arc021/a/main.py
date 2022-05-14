import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A = []
for _ in range(4):
    A.append(na())
for i in range(4):
    for j in range(4):
        if i + 1 < 4 and A[i][j] == A[i + 1][j]:
            print("CONTINUE")
            exit()
        if j + 1 < 4 and A[i][j] == A[i][j + 1]:
            print("CONTINUE")
            exit()
print("GAMEOVER")