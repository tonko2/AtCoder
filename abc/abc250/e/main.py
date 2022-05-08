import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

MOD = 10 ** 9 + 7

N = ni()
A = na()
B = na()
Q = ni()

SA = set()
SB = set()
sumA = [0] * (N + 1)
sumB = [0] * (N + 1)
multiA = [1] * (N + 1)
multiB = [1] * (N + 1)
cntA = [0] * (N + 1)
cntB = [0] * (N + 1)

for i in range(N):
    if A[i] not in SA:
        sumA[i + 1] = sumA[i] + A[i]
        multiA[i + 1] = (multiA[i] * A[i]) % MOD
        cntA[i + 1] = cntA[i] + 1
        SA.add(A[i])
    else:
        sumA[i + 1] = sumA[i]
        cntA[i + 1] = cntA[i]
        multiA[i + 1] = multiA[i]

    if B[i] not in SB:
        sumB[i + 1] = sumB[i] + B[i]
        multiB[i + 1] = (multiB[i] * B[i]) % MOD
        cntB[i + 1] = cntB[i] + 1
        SB.add(B[i])
    else:
        sumB[i + 1] = sumB[i]
        cntB[i + 1] = cntB[i]
        multiB[i + 1] = multiB[i]

for _ in range(Q):
    x, y = na()
    if sumA[x] == sumB[y] and cntA[x] == cntB[y]:
        if min(x, y) > 1 and multiA[x] != multiB[y]:
            print("No")
        else:
            print("Yes")
    else:
        print("No")