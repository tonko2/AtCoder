H, W = map(int, input().split())
A = [] * W
for i in range(H):
    A.append(list(map(int, input().split())))

for i in range(H - 1):
    for j in range(W - 1):
        if A[i][j] + A[i + 1][j + 1] > A[i + 1][j] + A[i][j + 1]:
            print("No")
            exit()

print("Yes")
