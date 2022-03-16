import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

ans = ['F', 'M', 'T']
V, A, B, C = na()
A = [A, B, C]
cur = 0
while V - A[cur] >= 0:
    V -= A[cur]
    cur = (cur + 1) % 3
print(ans[cur])