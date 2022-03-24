import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
A, B, C = 0, 0, 0
if len(S) == 1:
    print("YES")
    exit()
for c in S:
    if c == 'a':
        A += 1
    if c == 'b':
        B += 1
    if c == 'c':
        C += 1
min_v = min(A, B, C)
A -= min_v
B -= min_v
C -= min_v
arr = sorted([A, B, C])
if arr[1] == 1 and arr[2] == 1 or arr[1] == 1 and arr[2] == 0 or arr[1] == 0 and arr[2] == 1 or arr[1] == 0 and arr[2] == 0:
    print("YES")
else:
    print("NO")

