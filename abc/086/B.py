a, b = map(str, input().split())
for i in range(2, 1000):
    if i * i == int(a + b):
        print("Yes")
        exit()
print("No")
