N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
m.sort()
X -= sum(m)
print(N + X // m[0])
