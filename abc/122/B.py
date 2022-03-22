S = input()
S = S.replace("A", "*")
S = S.replace("C", "*")
S = S.replace("G", "*")
S = S.replace("T", "*")
ans = 0
for i in range(len(S), 0, -1):
    if S.count("*" * i) >= 1:
        ans = i
        break
print(ans)