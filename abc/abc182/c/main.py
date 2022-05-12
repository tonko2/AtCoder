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
s = str(N)
total = sum(map(int, str(N)))
ans = INF
for bit in range(1 << (len(str(N)))):
    total_tmp = total
    cnt = 0
    for i in range(len(str(N))):
        if bit & 1 << i:
            total_tmp -= int(s[i])
            cnt += 1
    if cnt == len(s):
        continue
    if total_tmp % 3 == 0:
        ans = min(ans, cnt)
if ans == INF:
    print(-1)
else:
    print(ans)
