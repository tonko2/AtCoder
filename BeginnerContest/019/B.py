S = list(input())
ans = ""
cnt = 1
now = S[0]
for i in range(1, len(S)):
    if now == S[i]:
        cnt += 1
    else:
        ans += now + str(cnt)
        now = S[i]
        cnt = 1
ans += now + str(cnt)

print(ans)
