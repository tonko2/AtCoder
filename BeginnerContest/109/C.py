import sys
from collections import defaultdict
import math

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, X = na()
x = na()
arr = []
for i in range(N):
    arr.append(abs(X - x[i]))
base = arr[0]
for i in range(1, len(arr)):
    base = math.gcd(base, arr[i])
print(base)