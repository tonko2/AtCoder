import sys
import math
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A = 60 * 21
K = ni()
A += K
B = A // 60
C = A % 60
if C < 10:
    C = '0' + str(C)
print(f'{B}:{C}')