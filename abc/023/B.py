N = int(input())
S = list(input())

ans = -1
if N % 2 == 0:
    ans = -1
else:
    while len(S):
        if S[0] == "b" and S[-1] == "b" or S[0] == "a" and S[-1] == "c" or S[0] == "c" and S[-1] == "a":
            S = S[1:-1]
            ans += 1
        else:
            break
    if len(S):
        ans = -1
print(ans)