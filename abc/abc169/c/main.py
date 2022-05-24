import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = input().split()
A = int(S[0])
B, C = S[1].split('.')
B = int(B)
C = int(C)
print(A * (B * 100 + C) // 100)