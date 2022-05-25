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
S = ns()

ans = 0
for i in range(1000):
    cur = 0
    s = str(i)
    if i < 10:
        s = "00" + s
    if 10 <= i < 100:
        s = "0" + s
    for j in range(N):
        if S[j] == s[cur]:
            cur += 1
        if cur == 3:
            ans += 1
            break
print(ans)