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
alpha = set()

lower_flag = False
for i, c in enumerate(S.lower()):
    if S[i] == c:
        lower_flag = True

upper_flag = False
for i, c in enumerate(S.upper()):
    if S[i] == c:
        upper_flag = True

for i, c in enumerate(S):
    alpha.add(c)

if len(alpha) != len(S) or lower_flag == False or upper_flag == False:
    print("No")
else:
    print("Yes")
