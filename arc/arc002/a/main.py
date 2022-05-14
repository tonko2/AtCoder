import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

Y = ni()
if Y % 4 == 0:
    if Y % 100 == 0:
        if Y % 400 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")