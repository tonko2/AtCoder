N, X = map(int, input().split())
X *= 100
total = 0
ans = -1
for i in range(N):
    v, p = map(int, input().split())
    total += v * p
    if ans == -1 and X < total:
        ans = i + 1

print(ans)