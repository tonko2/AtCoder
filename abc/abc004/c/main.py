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
N %= 30
A = ['1', '2', '3', '4', '5', '6']
for i in range(N):
    A[i % 5], A[i % 5 + 1] = A[i % 5 + 1], A[i % 5]
print("".join(A))