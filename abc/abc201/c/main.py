import itertools
import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def judge(num):
    for a in needs:
        if a not in num:
            return False
    return True

def dfs(cnt, num):
    if cnt == 4:
        if judge(num):
            ans.add(num)
        return

    for i in range(len(nums)):
        dfs(cnt + 1, num + nums[i])
S = ns()
if S.count("o") > 4 or S.count("x") == 10:
    print(0)
    exit()
nums = []
needs = []
ans = set()
for i in range(10):
    if S[i] == 'o' or S[i] == '?':
        if S[i] == 'o':
            needs.append(str(i))
        nums.append(str(i))
dfs(0, "")
print(len(ans))