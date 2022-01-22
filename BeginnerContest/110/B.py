N, M, A, B = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

for z in range(A+1, B+1):
    flag = True
    for x in X:
        if z <= x:
            flag = False
    for y in Y:
        if z > y:
            flag = False
    if flag:
        print("No War")
        exit()
print("War")