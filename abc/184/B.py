N, X = map(int, input().split())
S = input()

for c in S:
    if c == 'o':
        X += 1
    else:
        X = max(0, X - 1)

print(X)