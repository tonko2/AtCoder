import sys
import math
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
T = ns()
S_strs = []
S_nums = []
T_strs = []
T_nums = []
i = 0
while i < len(S):
    cnt = 1
    alpha = S[i]
    while i + 1 < len(S) and S[i] == S[i + 1]:
        cnt += 1
        i += 1
    i += 1
    S_strs.append(alpha)
    S_nums.append(cnt)
i = 0
while i < len(T):
    cnt = 1
    alpha = T[i]
    while i + 1 < len(T) and T[i] == T[i + 1]:
        cnt += 1
        i += 1
    i += 1
    T_strs.append(alpha)
    T_nums.append(cnt)

# print(S_strs)
# print(S_nums)
# print(T_strs)
# print(T_nums)

N = len(S_strs)
M = len(T_strs)
if N != M:
    print("No")
else:
    for i in range(N):
        if S_strs[i] != T_strs[i]:
            print("No")
            exit()
        if S_nums[i] == 1 and T_nums[i] > 1 or S_nums[i] > T_nums[i]:
            print("No")
            exit()
    print("Yes")