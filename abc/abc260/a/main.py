import sys
import math
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
memo = [0] * 26
for i in range(len(S)):
    memo[ord(S[i]) - ord('a')] += 1
for i in range(26):
    if memo[i] == 1:
        print(chr(ord('a') + i))
        exit()
print(-1)