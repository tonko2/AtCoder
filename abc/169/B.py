N = int(input())
A = list(map(int, input().split()))

limit = 1e18
ans = 1
if A.count(0) > 0:
    ans = 0
for a in A:
    ans *= a
    if ans > limit:
        print(-1)
        exit()
print(ans)