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
d = defaultdict(int)
S = []
for _ in range(N):
    S.append(ns())
    d[S[-1]] += 1

for s in S:
    if s[0] == '!':
        continue
    if d['!' + s]:
        print(s)
        exit()
print("satisfiable")
