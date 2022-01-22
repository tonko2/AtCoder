N = int(input())

total = 0
for i in range(N):
    x, y = map(str, input().split())
    if y == "JPY":
        total += int(x)
    else:
        total += float(x) * 380000
print(total)
