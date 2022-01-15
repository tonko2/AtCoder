A, B, C, D = map(int, input().split())
blue = A
red = 0
ans = 0

while blue > red * D:
    blue += B
    red += C
    ans += 1
    if blue - red * D <= (blue + B) - ((red + C) * D):
        ans = -1
        break

print(ans)