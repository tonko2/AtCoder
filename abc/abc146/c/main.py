import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def calc(n):
    d = len(str(n))
    return A * n + B * d <= X

A, B, X = na()
if B > X:
    print(0)
    exit()
left = 0
right = 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if calc(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)

