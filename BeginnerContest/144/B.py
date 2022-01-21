l = []
for i in range(1, 10):
    for j in range(1, 10):
        l.append(i * j)

N = int(input())

if N in l:
    print("Yes")
else:
    print("No")

