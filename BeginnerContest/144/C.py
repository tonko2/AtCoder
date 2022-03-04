import sys
import math

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, A, B = na()
if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    cnt = 0
    if A - 1 >= N - B:
        cnt = N - B + 1
        A += N - B + 1
        B = N
    else:
        cnt = A
        B -= A
        A = 1
    print(cnt + (B - A) // 2)