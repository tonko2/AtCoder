import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B, C = na()
C %= 2
if C == 0:
    if A < 0:
        A *= -1
    if B < 0:
        B *= -1
if A == B:
    print("=")
elif A > B:
    print(">")
else:
    print("<")
