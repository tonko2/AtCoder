S = list(map(str, input()))

for i in range(len(S)):
    if S[i] == '6':
        S[i] = '9'
    elif S[i] == '9':
        S[i] = '6'

S = reversed(S)
print("".join(S))