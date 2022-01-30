N = int(input())
stairs = [0] * (N + 1)
stairs[0] = 1
for i in range(0, N):
    if i + 1 <= N:
        stairs[i + 1] += stairs[i]
    if i + 2 <= N:
        stairs[i + 2] += stairs[i]
print(stairs[N])