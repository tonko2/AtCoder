
ans = 0
for i in range(3):
    s, e = map(int, input().split())
    ans += s * e

print(ans // 10)
