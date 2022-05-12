import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def base_10_to_n(x, n):
    res = []
    while x:
        res.append(str(x % n))
        x //= n
    res.reverse()
    return "".join(res)

N = ni()
ans = 0
for i in range(1, N + 1):
    a = base_10_to_n(i, 8)
    if '7' in str(a) or '7' in str(i):
        continue
    ans += 1
print(ans)