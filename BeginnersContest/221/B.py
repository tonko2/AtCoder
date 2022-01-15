S = list(map(str, input()))
T = list(map(str, input()))

strs = [S]
for i in range(len(S) - 1):
    strs.append(S[0:i] + S[i+1:i+2] + S[i:i+1] + S[i+2:])

if T in strs:
    print("Yes")
else:
    print("No")