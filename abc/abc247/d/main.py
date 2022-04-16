import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

Q = ni()
q = deque()
for i in range(Q):
    query = input().split()
    if len(query) == 3:
        _, x, c = query
        q.append((int(c), int(x)))
    else:
        _, c = query
        c = int(c)
        total = 0
        while c > 0:
            que_c, que_x = q.popleft()
            minus = min(c, que_c)
            total += que_x * minus
            c -= minus
            que_c -= minus
            if que_c > 0:
                q.appendleft((que_c, que_x))
        print(total)
