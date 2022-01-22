S = list(map(str, input()))

out = ''
for i in range(len(S)):
    if i % 2 == 0:
        out += S[i]
print(out)
