N = int(input())
ans = []
for i in range(2, N+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag:
        ans.append(i)
print(*ans)