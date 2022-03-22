S = []
for _ in range(4):
    S.append(input())
for i in range(4):
    print(S[3 - i][::-1])