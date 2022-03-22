A, B = map(int, input().split())

hole = 1
ans = 0
while hole < B:
    hole -= 1
    hole += A
    ans += 1

print(ans)