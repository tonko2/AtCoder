import sys
from collections import defaultdict
import math
import queue

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def prime_factors(N):
    rem = N
    res = []

    for i in range(2, int(math.sqrt(N)) + 1):
        while rem % i == 0:
            rem /= i
            res.append(i)

    if rem != 1:
        res.append(rem)
    return res

N = ni()
d = prime_factors(N)
for i in range(21):
    if 1 << i >= len(d):
        print(i)
        exit()
