N, P = map(int, input().split())
ans = 0
A = list(map(int, input().split()))
for x in A:
    if P > x:
        ans += 1

print(ans)

