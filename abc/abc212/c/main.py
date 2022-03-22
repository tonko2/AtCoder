import bisect
import sys
from collections import defaultdict
import bisect

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
A = na()
B = na()
A.sort()
B.sort()
ans = INF

for i in range(N):
    pos = max(0, bisect.bisect(B, A[i]) - 1)
    ans = min(ans, abs(A[i] - B[pos]), abs(A[i] - B[max(pos - 1, 0)]))
    #print(pos)
for i in range(M):
    pos = max(0, bisect.bisect(A, B[i]) - 1)
    ans = min(ans, abs(A[pos] - B[i]), abs(A[max(pos - 1, 0)] - B[i]))
    #print(pos)
print(ans)

