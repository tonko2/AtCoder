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
ans = []
while N:
    N -= 1
    ans.append(chr(ord('a') + (N % 26)))
    N //= 26
print("".join(ans[::-1]))