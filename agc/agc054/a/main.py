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
S = ns()
if S[0] != S[-1]:
    print(1)
else:
    c = S[0]
    for i in range(1, len(S) - 2):
        if S[i] != c and S[i + 1] != c:
            print(2)
            exit()
    print(-1)