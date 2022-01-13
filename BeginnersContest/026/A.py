A = int(input())
ans = 0
for i in range(1, A + 1):
    ans = max(ans, i * (A - i))
print(ans)