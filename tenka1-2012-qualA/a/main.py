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
fib = [1, 1]
for i in range(2, N + 1):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib[N])