N, X = map(int, input().split())
L = list(map(int, input().split()))
jump = [0] * (N + 1)
ans = 1
for i, x in enumerate(L):
    jump[i + 1] = jump[i] + L[i]
    if jump[i + 1] <= X:
        ans += 1
print(ans)
