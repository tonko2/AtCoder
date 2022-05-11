import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def divisor(n):
    sq = n**0.5
    border = int(sq)
    table = []
    bigs = []
    for small in range(1, border+1):
        if n%small == 0:
            table.append(small)
            big = n//small
            bigs.append(big)
    if border == sq:
        bigs.pop()
    table += reversed(bigs)
    return table

A, B = na()
ans = 1

for i in range(A, B + 1):
    d = divisor(i)
    for a in d:
        if i + a <= B:
            ans = max(ans, a)
print(ans)