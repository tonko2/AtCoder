import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

@lru_cache(maxsize=None)
def rec(h):
    if h == 0:
        return 1
    return rec(h // 2) + rec(h // 2)

H = ni()
print(rec(H) - 1)
