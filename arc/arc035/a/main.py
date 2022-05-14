import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
ans = ""
for i, s in enumerate(S):
    if S[len(S) - 1 - i] == '*' or s == '*':
        ans += '*'
    else:
        ans += s

if ans == ans[::-1]:
    print("YES")
else:
    print("NO")