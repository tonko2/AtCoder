n = int(input())
a = list(map(int, input().split()))
ans = 0
flag = True
while True:
    for i in range(n):
        if a[i] % 2 != 0:
            print(ans)
            exit()
        a[i] /= 2
    ans+=1



