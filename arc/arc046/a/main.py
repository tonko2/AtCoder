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
cnt = 0
nums = "123456789"
A = []
for i in range(9):
    for j in range(1, 10):
        A.append(int(nums[i] * j))
A.sort()
print(A[N - 1])