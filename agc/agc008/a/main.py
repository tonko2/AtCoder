import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

x, y = na()
ans = abs(abs(x) - abs(y))
if (x >= 0 and y >= 0 and x < y) or (x <= 0 and y <= 0 and x < y) or x == y:
    pass
elif x < 0 and y < 0 and x > y:
    ans += 2
elif x > 0 and y > 0 and x > y:
    ans += 2
else:
    ans += 1
print(ans)