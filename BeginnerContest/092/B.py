N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X
for a in A:
    if D % a == 0:
        ans -= 1
    ans += 1 + D // a
print(ans)
