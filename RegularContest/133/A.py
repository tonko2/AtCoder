N = int(input())
A = list(map(int, input().split()))

maxNum = A[-1]
for i in range(N-1):
    if A[i] > A[i+1]:
        maxNum = A[i]
        break

new_A = []
for a in A:
    if a == maxNum:
        continue
    new_A.append(a)
print(*new_A)