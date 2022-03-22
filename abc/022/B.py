N = int(input())
d = dict()
for _ in range(N):
    a = int(input())
    d[a] = d.get(a, 0) + 1
ans = 0
for a in d.keys():
    if d[a] > 1:
        ans += d[a] - 1
print(ans)
