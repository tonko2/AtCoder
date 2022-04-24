import collections
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W = na()
P = []
for _ in range(H):
    P.append(na())

ans = 1
for bit in range(1 << H):
    h = bin(bit).count("1")
    h_arr = []
    for i in range(H):
        if bit & 1 << i:
            h_arr.append(i)
    most = []
    for i in range(W):
        flag = True
        num = -1
        for j in h_arr:
            if num == -1:
                num = P[j][i]
            if P[j][i] != num:
                flag = False
                break
        if flag:
            most.append(num)
    most_common = collections.Counter(most).most_common()
    if len(most_common) == 0:
        continue
    k, v = most_common[0]
    if k != -1:
        ans = max(ans, h * v)
print(ans)
