import itertools
import sys
from collections import defaultdict
from itertools import permutations

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

tmp = ns().split()
S = tmp[0]
K = int(tmp[1])

S = sorted(S)
p = itertools.permutations(S)
d = defaultdict(int)
for s in p:
    d["".join(list(s))] += 1
all = []
for str in d.keys():
    all.append(str)
print(all[K - 1])