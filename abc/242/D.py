import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def g(c, add):
    return chr(ord('A') + (ord(c) - ord('A') + add) % 3)

def f(t, k):
    if t == 0:
        return S[k]
    if k == 0:
        return g(S[0], t)
    return g(f(t - 1, k // 2), k % 2 + 1)

S = ns()
Q = ni()
for i in range(Q):
    t, k = na()
    print(f(t, k - 1))
