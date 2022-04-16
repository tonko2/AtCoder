import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def calc(n):
    return n * (n + 1) // 2

N, X, Y = na()
A = na()
X_cnt = 0
Y_cnt = 0
for i in range(N):
    if A[i] == X:
        X_cnt += 1
    if A[i] == Y:
        Y_cnt += 1
l = 0
tmp_x_cnt = X_cnt
tmp_y_cnt = Y_cnt
while l < N and tmp_x_cnt and tmp_y_cnt:
    if A[l] == X:
        tmp_x_cnt -= 1
    if A[l] == Y:
        tmp_y_cnt -= 1
    l += 1

r = N - 1
tmp_x_cnt = X_cnt
tmp_y_cnt = Y_cnt
while r >= 0 and tmp_x_cnt and tmp_y_cnt:
    if A[r] == X:
        tmp_x_cnt -= 1
    if A[r] == Y:
        tmp_y_cnt -= 1
    r -= 1

# print(f'calc = {calc(N)}')
print(f'l = {l}, r = {r}')
ans = calc(N) - calc(N - l) - calc(r + 1)

print(ans)