import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
B = [[] for _ in range(K)]
for i in range(N):
    B[i % K].append(A[i])
for i in range(K):
    B[i].sort()
C = []
idx = 0
while True:
    flag = False
    for i in range(K):
        if len(B[i]) > idx:
            flag = True
            C.append(B[i][idx])
    idx += 1
    if flag == False:
        break
if C == sorted(A):
    print("Yes")
else:
    print("No")



