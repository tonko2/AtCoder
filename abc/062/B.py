H, W = map(int, input().split())
field = [list('#' * (W + 2)) for _ in range(H + 2)]
for i in range(H):
    A = list(input())
    for j, a in enumerate(A):
        field[i+1][j+1] = a
for i in range(H+2):
    print("".join(field[i]))