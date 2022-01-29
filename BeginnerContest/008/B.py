N = int(input())
d = dict()
ans = ""
cnt = 0
for _ in range(N):
    s = input()
    d[s] = d.get(s, 0) + 1
    if cnt < d[s]:
        ans = s
        cnt = d[s]
print(ans)

