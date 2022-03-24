import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
alpha = "abcdefghijklmnopqrstuvwxyz"
ans = INF
S2 = S
for c in alpha:
    S = S2
    cnt = 0
    while S.count(c) != len(S):
        tmp_S = ""
        for i in range(len(S) - 1):
            if S[i] == c or S[i + 1] == c:
                tmp_S += c
            else:
                tmp_S += S[i]
        S = tmp_S
        cnt += 1
    ans = min(ans, cnt)
print(ans)
