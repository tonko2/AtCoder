K = int(input())
ans = ""
while K != 1:
    if K % 2 == 1:
        ans += "2"
    else:
        ans += "0"
    K //= 2

ans += "2"
print(ans[::-1])
