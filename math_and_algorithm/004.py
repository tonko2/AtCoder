A = list(map(int, input().split()))
ans = 1
for a in A:
    ans *= a
print(ans)