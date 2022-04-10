import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
l = 0
r = N - 1
while l <= r:
    tmp_l = l
    tmp_r = r
    if l % 2 == 0:
        if A[r] == 0:
            r -= 1
        elif A[l] == 0:
            l += 1
    else:
        if A[r] == 1:
            r -= 1
        elif A[l] == 1:
            l += 1
    if tmp_l == l and tmp_r == r:
        print("No")
        exit()
print("Yes")