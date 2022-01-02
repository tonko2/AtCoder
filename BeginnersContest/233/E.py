# TLE
X = input()

ans = 0
for i in range(len(X)):
    ans += int(X[0:len(X) - i])

print(ans)
