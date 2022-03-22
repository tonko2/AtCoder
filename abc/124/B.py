N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(N):
    now = H[i]
    flag = True
    for j in range(i+1):
        if H[i] < H[j]:
            flag = False
    if flag:
        ans += 1
print(ans)