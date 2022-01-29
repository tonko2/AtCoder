X = input()
X = X.replace("ch", "")
X = X.replace("o", "")
X = X.replace("k", "")
X = X.replace("u", "")
if len(X) == 0:
    print("YES")
else:
    print("NO")