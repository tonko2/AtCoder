S = input()
for i, s in enumerate(S):
    if i % 2 == 1:
        if s == 'R':
            print("No")
            exit()
    else:
        if s == 'L':
            print("No")
            exit()
print("Yes")