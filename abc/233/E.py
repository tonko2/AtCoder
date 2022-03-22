X = list(map(int, list(input())))
s = sum(X)
X.reverse()
res = []
c = 0

for x in X:
    c += s
    res.append(c % 10)
    c = int(c / 10)
    s -= x

if c != 0:
    c += s
    res.append(c % 10)

print(''.join(list(map(str, res[: : -1]))))