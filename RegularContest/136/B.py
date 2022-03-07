import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def inversion_number(A, N):
    res = 0
    bit = Bit(N)

    for i, p in enumerate(A):
        bit.add(p, 1)
        res += i + 1 - bit.sum(p)
    return res

N = ni()
A = na()
B = na()
if sorted(A.copy()) != sorted(B.copy()):
    print("No")
    exit()

if len(set(A)) < N:
    print("Yes")
    exit()

if inversion_number(A, max(A)) % 2 == inversion_number(B, max(B)) % 2:
    print("Yes")
else:
    print("No")

