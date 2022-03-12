import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

K, A, B = na()
if A + 1 >= B:
    print(K + 1)
    exit()

ans = B
K -= (A + 1)

ans = ans - A * (K // 2) + B * (K // 2)
ans += K % 2
print(ans)