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
if abs(A) == abs(B):
    print("Draw")
elif abs(A) > abs(B):
    print("Bug")
else:
    print("Ant")
