import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
B = na()
ans_A = 0
ans_B = 0

for i in range(N):
    if A[i] == B[i]:
        ans_A += 1

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i] == B[j]:
            ans_B += 1

print(ans_A)
print(ans_B)