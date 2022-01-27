n = int(input())

ans = n
for i in range(1, n + 1):
    ans = min(ans, abs(n // i - i) + n % i)
print(ans)