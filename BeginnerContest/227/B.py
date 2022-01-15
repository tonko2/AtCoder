N = int(input())
S = list(map(int, input().split()))

def area(a, b):
    return 4 * a * b + 3 * a + 3 * b

areas = []

for i in range(1, 1000):
    for j in range(1, 1000):
        areas.append(area(i, j))

ans = 0

for i in range(N):
    if S[i] not in areas:
       ans += 1

print(ans)
