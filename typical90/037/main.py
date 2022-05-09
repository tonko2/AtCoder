import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

class SegTree:
    """
    Segment Tree
    """

    def __init__(self, init_val, segfunc=min, ide_ele=float('inf')):
        """
        初期化

        init_val: 配列の初期値
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新

        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る

        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

W, N = na()
L = [0] * N
R = [0] * N
V = [0] * N
for i in range(N):
    L[i], R[i], V[i] = na()

def segfunc(x, y):
    return max(x, y)
ide_ele = -1

seg = SegTree([-1] * (W + 2), segfunc=segfunc, ide_ele=ide_ele)
seg.update(0, 0)

for a in range(N):
    l, r, v = L[a], R[a], V[a]
    for i in range(W + 1)[::-1]:
        if i - l < 0:
            continue
        now = seg.query(i, i + 1)
        x = seg.query(max(0, i - r), i - l + 1)
        if x == -1:
            continue
        if now < x + v:
            seg.update(i, x + v)
print(seg.query(W, W + 1))