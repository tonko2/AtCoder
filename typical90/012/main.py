import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def query1(sx, sy):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        gx = sx + dx[i]
        gy = sy + dy[i]
        if used[gy][gx] == False:
            continue
        hash1 = (sy - 1) * W + (sx - 1)
        hash2 = (gy - 1) * W + (gx - 1)
        uf.union(hash1, hash2)
    used[sy][sx] = True

def query2(sx, sy, gx, gy):
    if used[sy][sx] == False or used[gy][gx] == False:
        return False

    hash1 = (sy - 1) * W + (sx - 1)
    hash2 = (gy - 1) * W + (gx - 1)

    if uf.same(hash1, hash2):
        return True
    return False


ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W = na()
Q = ni()
uf = UnionFind((H + 1) * (W + 1))
used = [[False] * (W + 2) for _ in range(H + 2)]
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        _, y, x = query
        y = int(y)
        x = int(x)
        query1(x, y)
    else:
        _, y1, x1, y2, x2 = query
        y1 = int(y1)
        x1 = int(x1)
        y2 = int(y2)
        x2 = int(x2)
        if query2(x1, y1, x2, y2):
            print("Yes")
        else:
            print("No")
