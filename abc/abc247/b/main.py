import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = []
T = []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)
for i in range(N):
    flag1 = False
    flag2 = False
    for j in range(N):
        if i == j:
            continue
        if S[i] == S[j] or S[i] == T[j]:
            flag1 = True
    for j in range(N):
        if i == j:
            continue
        if T[i] == S[j] or T[i] == T[j]:
            flag2 = True
    if flag1 and flag2:
        print("No")
        exit()
print("Yes")