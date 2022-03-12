import math

def prime_factors(N):
    rem = N
    res = []

    for i in range(2, int(math.sqrt(N)) + 1):
        while rem % i == 0:
            rem /= i
            res.append(i)

    if rem != 1:
        res.append(rem)
    return res