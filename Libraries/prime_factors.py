import math

def prime_factors(n):
    rem = n
    res = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while rem % i == 0:
            rem //= i
            res.append(i)
    if rem != 1:
        res.append(rem)
    return res

# N以下の素因数の種類を返す
def prime_kinds(N, K):
    cnt = [0] * (N + 1)
    for i in range(2, N + 1):
        if cnt[i] >= 1:
            continue
        j = i
        while j <= N:
            cnt[j] += 1
            j += i
    res = 0
    for i in range(1, N + 1):
        if cnt[i] >= K:
            res += 1
    return res