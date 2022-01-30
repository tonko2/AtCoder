N = int(input())
ans = 0
for _ in range(N):
    p, q = map(int, input().split())
    ans += (1 / p) * q
print(ans)