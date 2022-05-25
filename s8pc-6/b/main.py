import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def compress():
    C = []
    for i in range(N):
        C.append(A[i])
        C.append(B[i])
    D = sorted(set(C))
    return {v: i for i, v in enumerate(D)}

N = ni()
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = na()
d = compress()

ans = INF
for s in d.keys():
    for g in d.keys():
        cnt = 0
        for i in range(N):
            cnt += abs(s - A[i]) + abs(A[i] - B[i]) + abs(g - B[i])
        # print(f's = {s}, g = {g}, cnt = {cnt}')
        ans = min(ans, cnt)
print(ans)
