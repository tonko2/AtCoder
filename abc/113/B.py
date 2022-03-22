N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = -1
temperature = 1000

for i, h in enumerate(H):
    t = abs(T - H[i] * 0.006 - A)
    if t < temperature:
        temperature = t
        ans = i + 1
print(ans)