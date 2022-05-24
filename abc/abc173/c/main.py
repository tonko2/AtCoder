import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W, K = na()
grid = []
for _ in range(H):
    grid.append(ns())
total = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            total += 1

ans = 0
for bit_h in range(1 << H):
    cnt = 0
    for i in range(H):
        if bit_h & 1 << i:
            for j in range(W):
                if grid[i][j] == '#':
                    cnt += 1
    for bit_w in range(1 << W):
        cnt2 = 0
        for i in range(W):
            if bit_w & 1 << i:
                for j in range(H):
                    if bit_h & 1 << j:
                        continue
                    if grid[j][i] == '#':
                        cnt2 += 1
        if total - (cnt + cnt2) == K:
            ans += 1
print(ans)