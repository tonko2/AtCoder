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
A = list(map(int, input().split()))
total = [0] * N
total[0] = A[0]
d = defaultdict(int)
for i in range(1, N):
    total[i] = total[i - 1] + A[i]
for a in total:
    d[a] += 1

ans = 0
for a in d.keys():
    if d[a] >= 2:
        ans += combination(d[a], 2)
    if a == 0:
        ans += d[a]

print(ans)
