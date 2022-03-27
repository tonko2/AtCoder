import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, A, B, C, D = na()
S = ns()

for i in range(min(A, B) - 1, max(C, D) - 1):
    if S[i] == '#' and S[i + 1] == '#':
        print("No")
        exit()
if C < D:
    print("Yes")
else:
    for i in range(B - 2, D - 1):
        if S[i] == '.' and S[i + 1] == '.' and S[i + 2] == '.':
            print("Yes")
            exit()
    print("No")