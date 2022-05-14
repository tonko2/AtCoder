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
A = na()
odd = 0
for a in A:
    if a % 2:
        odd += 1
if odd % 2 == 0:
    print("YES")
else:
    print("NO")