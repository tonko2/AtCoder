import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10 ** 9 + 7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
if N == 1:
    print(0)
    exit()
ans = 1
for i in range(N - 2):
    ans = (ans * 10) % MOD
print((ans * 2) % MOD)