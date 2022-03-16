N = int(input())
X = 1
K = 0
while X <= N:
    X *= 2
    K += 1

print(max(0, K - 1))