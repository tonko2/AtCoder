import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def judge(x):
    prev = 0
    cnt = 0
    for i, a in enumerate(A):
        if a - prev >= x and L - a >= x:
            cnt += 1
            prev = a
    return cnt >= K

N, L = na()
K = ni()
A = na()
left = 0
right = L
while left <= right:
    mid = (left + right) // 2
    if judge(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)
