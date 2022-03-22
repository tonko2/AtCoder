X = int(input())

ans = 1
for i in range(2, 100):
    for j in range(2, 11):
        if i ** j <= X:
            ans = max(ans, i ** j)
print(ans)
