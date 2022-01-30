import math

N = int(input())
divisors = []
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N // i)
