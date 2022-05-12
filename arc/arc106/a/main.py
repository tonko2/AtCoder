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
for a in range(1, 100):
    for b in range(1, 100):
        v = 3 ** a + 5 ** b
        if v > N:
            break
        if v == N:
            print(a, b)
            exit()
print(-1)