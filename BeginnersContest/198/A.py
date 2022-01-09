N = int(input())
ans = 0
for i in range(1, N//2+1):
    if N - i == i:
        ans += 1
    else:
        ans += 2
print(ans)