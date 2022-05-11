import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

T = ni()
for _ in range(T):
    n = ni()
    if n % 2 == 0:
        if (n // 2) % 2 == 1:
            print("Same")
        else:
            print("Even")
    else:
        print("Odd")