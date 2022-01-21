N, L = map(int, input().split())
A = []
for i in range(N):
    A.append(L + (i + 1) - 1)

apple = 1000
for a in A:
    if abs(a) < abs(apple):
        apple = a

print(sum(A) - apple)