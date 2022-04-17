import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W = na()
A = []
B = []
for _ in range(H):
    A.append(na())
for _ in range(H):
    B.append(na())
for i in range(H):
    for j in range(W):
        A[i][j] -= B[i][j]

ans = 0

for i in range(H - 1):
    for j in range(W - 1):
        v = -A[i][j]
        A[i][j] += v
        A[i + 1][j] += v
        A[i][j + 1] += v
        A[i + 1][j + 1] += v
        ans += abs(v)

for i in range(H):
    for j in range(W):
        if A[i][j] != 0:
            print("No")
            exit()
print("Yes")
print(ans)