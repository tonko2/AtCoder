import itertools
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
P = na()
Q = na()
A = [i + 1 for i in range(N)]
d = defaultdict(int)
cnt = 1
a = 0
b = 0
for AA in itertools.permutations(A):
    if list(AA) == P:
        a = cnt
    if list(AA) == Q:
        b = cnt
    cnt += 1
print(abs(a - b))