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
B = na()
if sum(A) < sum(B):
    print(-1)
else:
    ans = 0
    diff = []
    need = 0
    for i in range(N):
        if A[i] >= B[i]:
            diff.append(A[i] - B[i])
        else:
            ans += 1
            need += B[i] - A[i]
    diff.sort()
    while need > 0 and diff:
        need -= diff[-1]
        diff.pop(-1)
        ans += 1
    print(ans)