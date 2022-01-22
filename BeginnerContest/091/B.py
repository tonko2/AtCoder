N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

ans = 0
d_s = dict()
d_t = dict()

for s in S:
    d_s[s] = d_s.get(s, 0) + 1
for t in T:
    d_t[t] = d_t.get(t, 0) + 1

for s in S:
    ans = max(ans, d_s[s] - d_t.get(s, 0))

print(ans)