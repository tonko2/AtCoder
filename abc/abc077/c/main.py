import bisect
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
A = sorted(na())
B = sorted(na())
C = sorted(na())
ans = 0
for i in range(N):
    b = B[i]
    a_cnt = bisect.bisect_left(A, b)
    c_cnt = N - bisect.bisect_right(C, b)
    ans += a_cnt * c_cnt
print(ans)