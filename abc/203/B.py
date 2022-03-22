N, K = map(int, input().split())

ans = 0
for i in range(N):
    ans += (100 * (i + 1)) * K + (K * (K + 1)) // 2

print(ans)