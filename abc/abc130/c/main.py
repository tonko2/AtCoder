import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

W, H, x, y = na()
ans1 = W * H / 2
ans2 = 0
if x * 2 == W and y * 2 == H:
    ans2 = 1
print(ans1, ans2)