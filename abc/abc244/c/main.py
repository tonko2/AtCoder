import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = set()
while True:
    for i in range(1, 2 * N + 2):
        if not i in S:
            print(i, flush=True)
            S.add(i)
            break
    a = ni()
    S.add(a)
    if a == 0:
        break