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
S = []
ans = INF
for _ in range(N):
    S.append(ns())
for i in range(0, 10):
    num = str(i)
    used = [False] * N
    cnt = 0
    for t in range(1001):
        for j in range(N):
            if used[j]:
                continue
            if S[j][(t % 10)] == num:
                used[j] = True
                cnt += 1
                break
        if cnt == N:
            # print(f'num = {num}, t = {t}')
            ans = min(ans, t)
            break
print(ans)