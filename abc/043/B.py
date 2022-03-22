S = list(input())
ans = ""

for c in S:
    if c == "B":
        ans = ans[0:-1]
    else:
        ans += c
print(ans)