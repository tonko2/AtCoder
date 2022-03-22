def judge(n, a, b):
    str_n = str(n)
    sum = 0
    for i in range(len(str_n)):
        sum += int(str_n[i])
    return a <= sum <= b

n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    if judge(i, a, b):
        ans += i

print(ans)