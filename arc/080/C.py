import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
four = 0
two = 0
for a in A:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two += 1

if four * 2 + 1 >= N or four * 2 + two >= N:
    print("Yes")
else:
    print("No")