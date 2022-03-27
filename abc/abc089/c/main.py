import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = [0, 0, 0, 0, 0] # MARCH cnt
for _ in range(N):
    s = ns()
    if s[0] == 'M':
        A[0] += 1
    if s[0] == 'A':
        A[1] += 1
    if s[0] == 'R':
        A[2] += 1
    if s[0] == 'C':
        A[3] += 1
    if s[0] == 'H':
        A[4] += 1

ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += A[i] * A[j] * A[k]
print(ans)
