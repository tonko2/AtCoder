N = int(input())
for i in range(1, 100000):
    if i * i > N:
        print((i - 1) ** 2)
        exit()