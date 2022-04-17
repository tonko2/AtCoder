import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = []
for _ in range(N):
    A.append(na())
total = 0
sum_A = []
for i in range(N):
    total += sum(A[i])
    sum_A.append(sum(A[i]))

ans = 0
for i in range(N):
    for j in range(6):
       ans = (ans + A[i][j] * (total - sum_A[i])) % MOD
print(ans)

