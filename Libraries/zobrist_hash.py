import sys
import math
from collections import defaultdict, deque
from random import randint

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()


r_map = {}
def gen_rand(A, B):
    for v in set(A + B):
        r_map[v] = randint(0, 10 ** 18)

# 整数の集合をHashで管理 {1, 2, 3} = {3, 1 ,2}
def hash(A):
    setA = set()
    s = 0
    r = [0]
    for a in A:
        if a not in setA:
            setA.add(a)
            s ^= r_map[a]
        r.append(s)
    return r

A = na()
B = na()
x, y = na()
gen_rand(A, B)
Ah = hash(A)
Bh = hash(B)
if Ah[x] == Bh[y]:
    print("Yes")
else:
    print("No")