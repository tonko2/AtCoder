from collections import defaultdict

def combination(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1

    tmp_n = 1
    for i in range(r):
        tmp_n *= n - i
    tmp_r = 1
    for i in range(r):
        tmp_r *= r - i
    return tmp_n // tmp_r

N = int(input())
K = 100000
A = list(map(int, input().split()))
ans = 0
d = defaultdict(int)
for a in A:
    d[a] += 1

for a in set(A):
    if a == 50000:
        ans += combination(d[a], 2)
        d[a] = 0
    else:
        ans += d[a] * d[K - a]
        d[K - a] = 0
print(ans)