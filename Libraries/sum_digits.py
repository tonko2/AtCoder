import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

# 2のN乗したあとの各桁の和を足した値
digits = [0] * 1000
digits[0] = 1
for i in range(1000):
    for j in range(1000):
        digits[j] *= 2
    for j in range(1000):
        if digits[j] >= 10:
            digits[j + 1] += digits[j] // 10
            digits[j] %= 10
print(sum(digits))