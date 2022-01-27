N = int(input())
S = []
P = []
ans = "atcoder"
for _ in range(N):
    s, p = map(str, input().split())
    S.append(s)
    P.append(int(p))
total = sum(P)
for i in range(N):
    if total < 2 * P[i]:
        ans = S[i]
print(ans)
