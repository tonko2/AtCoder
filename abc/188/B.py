N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

calc = 0
for i in range(N):
    calc += A[i] * B[i]

if calc == 0:
    print("Yes")
else:
    print("No")