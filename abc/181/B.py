N = int(input())
ans = 0

def sum(n):
    return n * (n + 1) // 2

for i in range(N):
    A, B = map(int, input().split())
    ans += sum(B) - sum(A-1)

print(ans)