import math
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
X = []
Y = []
for _ in range(N):
    x, y = na()
    X.append(x)
    Y.append(y)

orders = [i for i in range(N)]
ans = 0
for order in permutations(orders):
    order = list(order)
    for i in range(N - 1):
        a = order[i]
        b = order[i + 1]
        ans += math.sqrt((X[a] - X[b]) ** 2 + (Y[a] - Y[b]) ** 2)
print(ans / math.factorial(N))