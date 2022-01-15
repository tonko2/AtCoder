A, B, C = map(int, input().split())
cnt = 0
tmp = C
while C <= B:
    if A <= C <= B:
        print(C)
        exit()
    C += tmp
print(-1)