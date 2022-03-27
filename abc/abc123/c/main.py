import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = ni()
B = ni()
C = ni()
D = ni()
E = ni()

print(4 + (-(-N // min(A, B, C, D, E))))