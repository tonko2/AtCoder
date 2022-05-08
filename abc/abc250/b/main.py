import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, A, B = na()
ans = [[None] * (N * B) for _ in range(N * A)]
flag = 1
for a in range(N):
    for i in range(N):
        for j in range(A):
            for k in range(B):
                if i % 2 == 0 and a % 2 == 0:
                    ans[a * A + j][i * B + k] = '.'
                if i % 2 == 0 and a % 2 != 0:
                    ans[a * A + j][i * B + k] = '#'
                if i % 2 != 0 and a % 2 == 0:
                    ans[a * A + j][i * B + k] = '#'
                if i % 2 != 0 and a % 2 != 0:
                    ans[a * A + j][i * B + k] = '.'

for i in range(A * N):
    str = ""
    for c in ans[i]:
        str += c
    print(str)
