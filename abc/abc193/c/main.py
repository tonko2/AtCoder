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
ans = 0
S = set()
for i in range(2, int(math.sqrt(N)) + 1):
    for j in range(2, 40):
        if i ** j <= N and i ** j not in S:
            ans += 1
            S.add(i ** j)
        else:
            break
print(N - ans)