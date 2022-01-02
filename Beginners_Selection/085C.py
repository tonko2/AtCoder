N, Y = map(int, input().split())

for i in range(N+1):
    for j in range(N+1):
        k = N - i - j
        if i + j > N:
            break
        if 10000 * i + 5000 * j + 1000 * k == Y:
            print(f'{i} {j} {k}')
            exit()

print('-1 -1 -1')