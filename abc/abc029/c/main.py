import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(cnt, s):
    if cnt == N:
        ans.append(s)
    else:
        for i in range(3):
            dfs(cnt + 1, s + str[i])
N = ni()
str = ['a', 'b', 'c']
ans = []
dfs(0, "")
for s in ans:
    print(s)