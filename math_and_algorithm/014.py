import math

def isPrime(x):
    if x == 1 or x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
       if x % i == 0:
           return False
    return True

N = int(input())
ans = []
while not isPrime(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            ans.append(i)
            N //= i
            break
ans.append(N)
print(*ans)