N = int(input())
S = list(input())
ans = 0
x = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)