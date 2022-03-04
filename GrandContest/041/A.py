import sys
import math

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

N = ni()
if is_prime(N):
    print(N - 1)
else:
    ans = float('inf')
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            ans = min(ans, i - 1 + N // i - 1)
    print(ans)