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
ans = []
for i in range(N):
    cnt = 0
    remove = -1
    for j in range(N):
        if A[j] > 0:
            cnt += 1
            if A[j] == cnt:
                remove = j
    if remove == -1:
        print(-1)
        exit()
    ans.append(A[remove])
    A[remove] = 0
ans.reverse()
for a in ans:
    print(a)