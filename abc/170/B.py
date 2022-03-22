X, Y = map(int, input().split())

for i in range(0, 101):
    for j in range(0, 101):
        if 2 * i + 4 * j == Y and i + j == X:
            print("Yes")
            exit()
print("No")