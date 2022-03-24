import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x = 0
y = 0
cur = 0
N = ni()
T = ns()
for c in T:
    if c == 'R':
       cur = (cur + 1) % 4
    else:
        x += dx[cur]
        y += dy[cur]
print(x, y)