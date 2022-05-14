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
R = 0
B = 0
for _ in range(N):
    S = ns()
    R += S.count("R")
    B += S.count("B")
if R > B:
    print("TAKAHASHI")
elif R < B:
    print("AOKI")
else:
    print("DRAW")