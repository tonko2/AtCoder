import bisect
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
B = na()
C = na()
A.sort()
B.sort()
C.sort()
ans = 0
for i in range(N):
    now = A[i]
    idx = bisect.bisect_left(B, now + 1)
    if idx >= N or idx < i:
        continue
    now = B[idx]
    idx2 = bisect.bisect_left(C, now + 1)
    if idx2 >= N or idx2 < i:
        continue
    B[idx] = -1
    C[idx2] = -1
    ans += 1
print(ans)