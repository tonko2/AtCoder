S = input()
T = input()

ans = 0
for i in range(len(S) - len(T) + 1):
    S1 = S[i:i+len(T)]
    cnt = 0
    for j in range(len(T)):
        if S1[j] == T[j]:
            cnt += 1
    ans = max(ans, cnt)

print(len(T) - ans)
