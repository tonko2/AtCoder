N = input()
for i in range(10):
    S = "0" * i + N
    if S == S[::-1]:
        print("Yes")
        exit()
print("No")