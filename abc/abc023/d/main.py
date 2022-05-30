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
H = []
S = []
for _ in range(N):
    h, s = na()
    H.append(h)
    S.append(s)
left = 0
right = 10 ** 18


def judge(x):
    A = []
    for i in range(N):
        A.append((x - H[i]) // S[i])
    A.sort()
    for i in range(N):
        if i > A[i]:
            return False
    return True
while left <= right:
    mid = (left + right) // 2
    if judge(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)