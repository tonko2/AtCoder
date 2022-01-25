O = list(input())
E = list(input())
ans = []
for i in range(min(len(O), len(E))):
    ans.append(O[i] + E[i])
if len(O) > len(E):
    ans.append(O[-1])
elif len(O) < len(E):
    ans.append(E[-1])
print("".join(ans))