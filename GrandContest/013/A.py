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
ans = 1

i = 0
while i < N - 1:
    cur = A[i]
    j = i + 1
    order = 0 # -1 -> decrease, 0 -> TBD, 1 -> increase
    while j < N:
        if cur == A[j]:
            pass
        elif (order == 0 or order == 1) and cur < A[j]:
            order = 1
        elif (order == 0 or order == -1) and cur > A[j]:
            order = -1
        else:
            ans += 1
            i = j
            break
        cur = A[j]
        j += 1
        i = j
print(ans)