w = list(input())
d = dict()
for c in w:
    d[c] = d.get(c, 0) + 1
for c in w:
    if d[c] % 2 == 1:
        print("No")
        exit()
print("Yes")

