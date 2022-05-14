import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
N = len(S)
W = ni()
for i in range(N // W):
    print(S[i * W:i * W + W])
if N % W:
    print(S[W * (N // W):])