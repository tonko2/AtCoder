import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
d = defaultdict(int)
S = set(A)
for a in A:
    d[a] += 1

if max(A) == 0:
    print("Yes")
    exit()
if N % 3 != 0:
    print("No")
else:
    if len(S) == 2:
        if d[0] == N // 3:
            print("Yes")
        else:
            print("No")
    elif len(S) == 3:
        keys = [key for key in S]
        xor = 1
        for key in keys:
            xor ^= key
        if xor != 1:
            print("No")
            exit()
        else:
            if d[keys[0]] == N // 3 and d[keys[1]] == N // 3 and d[keys[2]] == N // 3:
                print("Yes")
            else:
                print("No")
    else:
        print("No")
