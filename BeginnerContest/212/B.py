X = list(map(str, input()))

if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
    print("Weak")

else:
    for i in range(3):
        X1 = ord(X[i]) - ord('0')
        X2 = ord(X[i+1]) - ord('0')
        if X2 == 0:
            X2 = 10
        if X1 != X2 - 1:
            print("Strong")
            exit()
    print("Weak")