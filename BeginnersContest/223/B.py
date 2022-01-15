S = input()
strs = [S]
for i in range(len(S) - 1):
    S = S[1:] + S[0]
    strs.append(S)

strs = sorted(strs)
print(strs[0])
print(strs[len(strs) - 1])