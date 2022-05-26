import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

R, C = na()
RC = []
for i in range(R):
    RC.append(na())

ans = 0
for bit in range(1 << R):
    cnt = 0
    for i in range(C):
        cnt_r = 0
        for j in range(R):
            if bit & 1 << j:
                cnt_r += 1 - RC[j][i]
            else:
                cnt_r += RC[j][i]
        cnt += max(cnt_r, R - cnt_r)
    ans = max(ans, cnt)
print(ans)