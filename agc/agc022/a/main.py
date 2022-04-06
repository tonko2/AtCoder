import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
if len(S) <= 25:
    for i in range(26):
        c = chr(ord('a') + i)
        if c not in S:
            print("".join(S) + c)
            exit()
if "".join(S) == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()
tmp = []
idx = 0
for i in range(25, 0, -1):
    tmp.append(S[i])
    if S[i - 1] < S[i]:
        idx = i - 1
        break
tmp.sort()
for c in tmp:
    if S[idx] < c:
        print("".join(S[:idx]) + c)
        exit()
