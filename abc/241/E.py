import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
ans = 0
now = 0
used = [0]
used2 = defaultdict(int)
used2[0] += 1

if K < 100000:
    for i in range(K):
        ans += A[now]
        now = ans % N
    print(ans)
    exit()

for i in range(K):
    ans += A[now]
    now = ans % N
    if used2[now] > 0:
        break
    used.append(now)
    used2[now] += 1

flag = False
S = []
ans = 0
for a in used:
    if a == now:
        flag = True
    if flag:
        S.append(a)
    else:
        ans += A[a]

total = 0
for a in S:
    total += A[a]

ans += total * ((K - (len(used) - len(S))) // len(S))
K = (K - (len(used) - len(S))) % len(S)

for i in range(K):
    ans += A[S[i]]

print(ans)