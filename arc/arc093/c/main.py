import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
dis = 0
x = 0
for a in A:
    dis += abs(x - a)
    x = a
dis += abs(x)
B = [0] + A + [0]
for i in range(1, N + 1):
    a = B[i - 1]
    b = B[i]
    c = B[i + 1]
    ans = dis - abs(a - b) - abs(b - c) + abs(a - c)
    print(ans)