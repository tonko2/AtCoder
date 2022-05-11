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
b = 0
ans = INF
while N >= (2 ** b):
    a = N // (2 ** b)
    c = N % (2 ** b)
    ans = min(ans, (a + b + c))
    b += 1
print(ans)