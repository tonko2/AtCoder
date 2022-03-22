import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def is_odd(A):
    for a in A:
        if a % 2 != 0:
            return True
    return False

A = na()
A.sort()
d = defaultdict(bool)
cnt = 0
while not d[tuple(A)]:
    if is_odd(A):
        print(cnt)
        exit()
    d[tuple(A)] = True
    A[0], A[1], A[2] = (A[1] + A[2]) // 2, (A[0] + A[2]) // 2, (A[0] + A[1]) // 2
    cnt += 1

print(-1)