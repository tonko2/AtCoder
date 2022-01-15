N, X = map(int, input().split())
A = list(map(int, input().split()))
total = 0
for i in range(N):
    total += A[i]
    if i % 2 == 1:
        total -= 1
if total <= X:
    print("Yes")
else:
    print("No")