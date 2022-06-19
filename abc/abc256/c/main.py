import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

h1, h2, h3, w1, w2, w3 = na()
A = [h1, h2, h3, w1, w2, w3]

S1 = set()
S2 = set()
S3 = set()
for i in range(1, 29):
    for j in range(1, 29):
        for k in range(1, 29):
            if i + j + k == h1:
                S1.add((i, j, k))
            if i + j + k == h2:
                S2.add((i, j, k))
            if i + j + k == h3:
                S3.add((i, j, k))

ans = 0
for s in S1:
    for s2 in S2:
        for s3 in S3:
            if s[0] + s2[0] + s3[0] == w1 and s[1] + s2[1] + s3[1] == w2 and s[2] + s2[2] + s3[2] == w3:
                ans += 1
print(ans)