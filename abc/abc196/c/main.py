import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

digits_str = "0123456789"

def dfs(str, cnt, N):
    if cnt == N:
        if str[0] == '0':
            return
        digits.append(str)
    else:
        for i in range(10):
            dfs(str + digits_str[i], cnt + 1, N)

N = ni()
ans = 0
digits = []
for i in range(1, 7):
    digits = []
    dfs("", 0, i)
    for s in digits:
        if int(s + s) <= N:
            ans += 1
print(ans)