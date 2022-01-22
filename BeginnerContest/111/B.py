N = int(input())

for i in range(N, 1000):
    if str(i) == str(i // 100) * 3:
        print(i)
        exit()