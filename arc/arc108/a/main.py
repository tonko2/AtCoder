import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S, P = na()
M = 1
while True:
    if M * (S - M) > P:
        print("No")
        break
    if M * (S - M) == P:
        print("Yes")
        break
    M += 1