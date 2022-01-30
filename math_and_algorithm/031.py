N = int(input())
A = list(map(int, input().split()))
dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)

for i in range(0, N):
    dp1[i + 1] = dp2[i] + A[i]
    dp2[i + 1] = max(dp1[i], dp2[i])

ans = max(dp1[N], dp2[N])
print(ans)
print(dp1)
print(dp2)