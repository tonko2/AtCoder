import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M, A, B = na()
for i in range(M):
    if N <= A:
        N += B
    c = ni()
    N -= c
    if N < 0:
        print(i + 1)
        exit()

print("complete")