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
A = na()
ans = INF
for bit in range(1 << (N - 1)):
    or_v = 0
    xor_v = 0
    for i in range(N):
        or_v |= A[i]
        if bit & 1 << i:
            xor_v ^= or_v
            or_v = 0
    if or_v:
        xor_v ^= or_v
    ans = min(ans, xor_v)

print(ans)