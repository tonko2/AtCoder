import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

a, b, c = na()
left = 2 * b
right = a + c
ans = 0
if left > right:
    ans = left - right
if left < right:
    ans = -(-(right - left) // 2) + (right - left) % 2
print(ans)
