import collections
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def calc(a, b, n):
    res = n - a.most_common()[0][1]
    a_key = a.most_common()[0][0]
    flag = False
    for (key, cnt) in b.most_common():
        if a_key != key:
            res += n - cnt
            flag = True
            break
    if flag == False:
        res += n
    return res
N = ni()
V = na()
A = collections.Counter(V[::2])
B = collections.Counter(V[1::2])
print(min(calc(A, B, N // 2), calc(B, A, N // 2)))
