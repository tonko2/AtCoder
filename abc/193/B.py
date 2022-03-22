N = int(input())
ans = 1e10
m = []
for i in range(N):
    A, P, X = map(int, input().split())
    m.append((A, P, X))

m.sort()

for i in range(N):
    A, P, X = m[i]
    if X - A > 0:
        ans = min(ans, P)

if ans == 1e10:
    ans = -1
print(ans)