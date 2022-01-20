N = int(input())
prime = [ True ] * (N + 1)

LIMIT = int(N ** 0.5)
for i in range(2, LIMIT + 1):
    if prime[i] == True:
        for j in range(2 * i, N + 1, i):
            prime[j] = False

for i in range(2, N + 1):
    if prime[i] == True:
        print(i)