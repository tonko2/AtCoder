import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def eratosthenes(N):
    prime = [ True ] * (N + 1)
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        if prime[i] == True:
            for j in range(2 * i, N + 1, i):
                prime[j] = False
    return prime

N = ni()
tmp_N = N
N = min(10 ** 6, N)
l = eratosthenes(N)
primes = []
for i in range(2, N):
    if l[i]:
        primes.append(i)

ans = 0
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        p = primes[i]
        q = primes[j]
        if p * (q ** 3) <= tmp_N:
            ans += 1
        else:
            break
print(ans)
