import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 100000

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def f(x):
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
    return res

N, K = na()
nxt = [0] * 100000
for i in range(100000):
    nxt[i] = (i + f(i)) % MOD

time_stamp = [-1] * 100000
pos = N
cnt = 0
while time_stamp[pos] == -1:
    time_stamp[pos] = cnt
    pos = nxt[pos]
    cnt += 1
cycle = cnt - time_stamp[pos]
if K >= time_stamp[pos]:
    K = (K - time_stamp[pos]) % cycle + time_stamp[pos]

ans = -1
for i in range(100000):
    if time_stamp[i] == K:
        ans = i
print(ans)