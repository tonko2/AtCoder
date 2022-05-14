import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

E = na()
B = ni()
L = na()
d = defaultdict(int)
for e in E:
    d[e] += 1
cnt = 0
bonus = False

for l in L:
    if d[l]:
        cnt += 1
        d[l] -= 1
    else:
        d[l] += 1
if d[B]:
    bonus = True

if cnt == 6:
    print(1)
elif cnt == 5 and bonus:
    print(2)
elif cnt == 5:
    print(3)
elif cnt == 4:
    print(4)
elif cnt == 3:
    print(5)
else:
    print(0)
