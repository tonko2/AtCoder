import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def dfs(deq, n):
    if n == 3:
        deq2 = deq.copy()
        exp = ""
        for i in range(3):
            exp += S[i] + deq2.popleft()
        exp += S[3]
        if eval(exp) == 7:
            print(exp + "=7")
            exit()
        else:
            return
    deq.append('+')
    dfs(deq, n + 1)
    deq.pop()
    deq.append('-')
    dfs(deq, n + 1)
    deq.pop()

S = ns()
q = deque()
dfs(q, 0)