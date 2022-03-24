S = input()
S = S[0:-1]
ans = 1
while len(S) > 0:
    if len(S) % 2 == 0:
        if S[0:len(S)//2] == S[len(S)//2:]:
            print(len(S))
            exit()
    S = S[0:-1]
print(ans)