import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

# 自分含め, 子ノードの数を数える
def dfs(pos, pre):
    tree[pos] = 1
    for v in G[pos]:
        if v == pre:
            continue
        dfs(v, pos)
        tree[pos] += tree[v]

N = 12
tree = [0] * N
G = [[] for _ in range(N)]
nodes = [(1, 2), (3, 1), (4, 2), (2, 5), (3, 6), (3, 7), (8, 4), (4, 9), (10, 5), (11, 7), (7, 12)]
A = [0] * (N - 1)
B = [0] * (N - 1)
for i in range(N - 1):
    a, b = nodes[i]
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dfs(0, -1)
print(tree)