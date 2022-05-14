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
S = S.lower()
I = -1
C = -1
T = -1
for i, s in enumerate(S):
    if I == -1 and s == 'i':
        I = i
    if C == -1 and I != -1 and I < i and s == 'c':
        C = i
    if s == 't':
        T = i
if I < C < T:
    print("YES")
else:
    print("NO")