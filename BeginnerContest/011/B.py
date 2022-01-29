S = list(input())
S[0] = S[0].upper()
for i in range(1, len(S)):
    S[i] = S[i].lower()
print("".join(S))