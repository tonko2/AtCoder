import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

str = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#', 'La', 'La#', 'Si']
str2 = "WBWBWWBWBWBWWBWBWWBW"
d = dict()
for i in range(12):
    d[str[i]] = str2[i]

S = ns()
for i in range(12):
    s = ""
    for j in range(20):
        s += d[str[(i + j) % 12]]
    if S == s:
        print(str[i])
        exit()