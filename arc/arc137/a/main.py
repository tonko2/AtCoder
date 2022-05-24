import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

L, R = na()
S = set()
for s in range(R - L):
    for x in range(s + 1):
        a = L + x
        b = R - (s - x)
        # print(f'a = {a}, b = {b}')
        if math.gcd(a, b) == 1:
            print(b - a)
            exit()