n = int(input())
isOk = [0] * 10
isOk[1] = True
isOk[3] = True
isOk[7] = True
isOk[9] = True
A = list(map(int, input().split()))
ans = 0
for a in A:
    cnt = 0
    while not isOk[a]:
        a -= 1
        cnt += 1
    ans += cnt
print(ans)

