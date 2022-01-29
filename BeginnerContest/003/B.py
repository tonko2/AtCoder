S = input()
T = input()
wild = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    if T[i] != S[i]:
        if S[i] == '@':
            if T[i] not in wild:
                print("You will lose")
                exit()
        elif T[i] == '@':
            if S[i] not in wild:
                print("You will lose")
                exit()
        else:
            print("You will lose")
            exit()

print("You can win")