N = int(input())
D = []
for i in range(N):
    a, b = map(int, input().split())
    D.append((a, b))

for i in range(N-2):
    a, b = D[i]
    a2, b2 = D[i+1]
    a3, b3 = D[i+2]
    if a == b and a2 == b2 and a3 == b3:
        print("Yes")
        exit()

print("No")