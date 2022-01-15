N, K, A = map(int, input().split())

cnt = 0
K -= 1
while K:
    if A + 1 > N:
        A = 1
    else:
        A += 1
    K -= 1
print(A)
