X, Y = map(int, input().split())

Y -= X
ans = 0
if Y > 0:
    ans += int(Y / 10)
    if Y % 10 > 0:
        ans += 1
print(ans)