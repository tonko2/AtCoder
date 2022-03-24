import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = list(map(str, input().split()))
T = list(map(str, input().split()))
cnt = 0
for i in range(3):
    if S[i] != T[i]:
        cnt += 1
if cnt == 0 or cnt == 3:
    print("Yes")
else:
    print("No")