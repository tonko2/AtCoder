import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
P = na()
Q = na()
A = sorted(P)


a = -1
b = -1
for i, p_a in enumerate(permutations(A)):
    if list(p_a) == P:
        a = i + 1
    if list(p_a) == Q:
        b = i + 1
print(abs(a - b))
